from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

import shop.views

app_name = shop

urlpatterns = [
    url(r'^$', shop.views.IndexListView.as_view(), name='home'),
    url(r'^product/(?P<pk>[0-9]+)$', shop.views.ProductDetailView.as_view(), name='product-detail'),
    url(r'^product/(?P<pk>[0-9]+)/buy$', shop.views.ProductBuyView.as_view(), name='product-buy'),
    url(r'^product/order$', shop.views.OrderView.as_view(), name='order'),

    url(r'^manage$', shop.views.ProductsListManageView.as_view(), name='product-list-manage'),
    url(r'^manage/create$', shop.views.ProductCreateView.as_view(), name='product-create'),
    url(r'^manage/(?P<pk>[0-9]+)/update$', shop.views.ProductUpdateView.as_view(), name='product-update'),
    url(r'^manage/(?P<pk>[0-9]+)/remove$', shop.views.ProductRemoveView.as_view(), name='product-remove'),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
