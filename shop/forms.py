from django import forms
from .models import Product, Cart

class IndexListForm(forms.Form):
    title =  forms.CharField(
                    required = False,
                    label='Title',
                    widget=forms.TextInput(attrs={'placeholder': 'Title'})
                  )
    producent =  forms.CharField(
                    required = False,
                    label='Producent',
                    widget=forms.TextInput(attrs={'placeholder': 'Producent'})
                  )

class ProductsManageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'producent', 'description', 'price', 'image']

class BuyManageForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['amount', 'order', 'product']