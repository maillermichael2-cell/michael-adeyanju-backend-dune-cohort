from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'category', 'image']
        widgets = { # lets you customze how each fields enders in HTML.
            'name': forms.TextInput(attrs={'placeholder': 'Product name'}),
            'price': forms.NumberInput(attrs={'min': '0', 'placeholder': 'Product Price'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__' # includes all editable fields on the model
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Category Name'}),
            'description': forms.TextInput(attrs={'placeholder': 'Category Description'})
        }