import os
import random
from datetime import datetime, timedelta
from tempfile import NamedTemporaryFile

from braces.views import GroupRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView
from InvoiceGenerator.api import Client, Creator, Invoice, Item, Provider
from InvoiceGenerator.pdf import ProformaInvoice

from .forms import IndexListForm, ProductsManageForm
from .models import Cart, Order, Product, Address
from .provider_adress import summary_provider, adress_provider, city_provider ,zipCode_provider


class IndexListView(ListView, FormView):
    model = Product
    template_name = 'shop/index.html'
    paginate_by = 3
    ordering = ['title']
    form_class = IndexListForm

    def get_queryset(self):
        queryset = super(IndexListView, self).get_queryset()
        if 'title' in self.request.GET:
            queryset = queryset.filter(
                title__contains=self.request.GET['title'])
        if 'producent' in self.request.GET:
            queryset = queryset.filter(
                producent__contains=self.request.GET['producent'])
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'


class ProductBuyView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cart
    fields = ['amount', ]
    template_name = None
    success_url = reverse_lazy('home')
    group_required = u"Client"
    success_message = 'You added the product to your cart.'

    def form_valid(self, form):
        order = Order.objects.filter(client=self.request.user).filter(
            dateOfPurchase__isnull=True)

        if order.exists():
            order = order.first()
        else:
            order = Order.objects.create(client=self.request.user)

        obj = form.save(commit=False)
        obj.order = order
        obj.product_id = self.kwargs['pk']

        obj.save()
        return super().form_valid(form)


class OrderView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'shop/order.html'
    group_required = u"Client"

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)

        obj = Order.objects.filter(client=self.request.user).filter(
            dateOfPurchase__isnull=True).first()
        if (not obj):
            context['price'] = 0
            return context

        obj.paymentDate = datetime.now() + timedelta(days=10)
        obj.dateOfPurchase = datetime.now()

        # Invoice generator
        client = Address.objects.filter(client=self.request.user).first()
        summary_client = client.company+" " + client.firstName+" " + client.surname
        adress_client = client.street+" " + str(client.houseNumber) +" " + str(client.apartmentNumber)
        city_client = client.city
        zipcode_client = client.zipCode
        client_obj = Client(summary_client, address = adress_client, city = city_client, zip_code = zipcode_client)

        provider_obj = Provider(summary_provider, address = adress_provider, city = city_provider, zip_code = zipCode_provider)
        
        creator_obj = Creator('John Doe')

        os.environ["INVOICE_LANG"] = "pl"
        invoice = Invoice(client_obj, provider_obj, creator_obj)
        invoice.currency = u'zł'
        invoice.currency_locale = 'pl.UTF-8'

        cart = Cart.objects.filter(order=obj)
        for product in cart:
            obj.price += product.product.price * product.amount
            invoice.add_item(Item(product.amount, product.product.price,
                                  description=product.product.title, tax=15))

        obj.save()

        # Invoice to pdf
        pdf = ProformaInvoice(invoice)
        pdf_name="invoice/"+summary_client+"invoice.pdf"
        pdf.gen(pdf_name)

        # Email send
        email = EmailMessage(
            'Purchase',
            'The purchase was successful',
            'from@example.com',
            [obj.client.email, ]
        )
        email.attach_file(pdf_name)
        email.send()

        context['price'] = obj.price
        return context


class ProductsListManageView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    model = Product
    template_name = 'shop/myproducts/product_list_manage.html'
    paginate_by = 3
    ordering = ['title']
    group_required = u"Seller"

    def get_queryset(self):
        queryset = super(ProductsListManageView, self).get_queryset().filter(
            seller=self.request.user)
        return queryset


class ProductUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    model = Product
    form_class = ProductsManageForm
    template_name = 'shop/myproducts/product_update.html'
    success_url = reverse_lazy('product-list-manage')
    group_required = u"Seller"

    def get_object(self, queryset=None):
        obj = super(ProductUpdateView, self).get_object()
        if not obj.seller == self.request.user:
            raise PermissionDenied("Permission Denied")
        if 'image' in self.request.FILES:
            obj.image = self.request.FILES['image']
            obj.save()
        return obj


class ProductCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    model = Product
    form_class = ProductsManageForm
    template_name = 'shop/myproducts/product_create.html'
    success_url = reverse_lazy('product-list-manage')
    group_required = u"Seller"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.seller = self.request.user
        if 'image' in self.request.FILES:
            obj.image = self.request.FILES['image']
        obj.save()
        return redirect('product-list-manage')


class ProductRemoveView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    model = Product
    template_name = 'shop/myproducts/product_confirm_delete.html'
    success_url = reverse_lazy('product-list-manage')
    group_required = u"Seller"

    def get_object(self, queryset=None):
        obj = super(ProductRemoveView, self).get_object()
        if not obj.seller == self.request.user:
            raise PermissionDenied("Permission Denied")
        return obj
