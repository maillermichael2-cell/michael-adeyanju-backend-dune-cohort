from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Product, Category
from django.db.models import Count
from django.http import HttpResponse

# Create your views here.

def home(request):
    featured_products = Product.objects.all()[:3]
    context = {'featured_products': featured_products}
    return render(request, 'products/home.html', context)

def about(request):
    return render(request, 'products/about.html')

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.annotate(product_count=Count('products'))
    context = {'products': products, 'categories': categories}
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


def category_list(request):
    categories = Category.objects.annotate(product_count=Count('products'))
    context = {'categories': categories}
    return render(request, 'products/category_list.html', context)

def page_not_found(request, undefined_path=None, execption=None):
    detail = undefined_path or str(execption) or 'Unknown error'
    return HttpResponse(f'Error 404: {detail}', content_type="text/plain", status=404)