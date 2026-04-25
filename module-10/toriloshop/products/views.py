from django.shortcuts import render,get_object_or_404, redirect
from .models import Product, Category
from django.db.models import Count
from django.http import HttpResponse
from django.contrib import messages
from .forms import ProductForm, CategoryForm


# Create your views here.

def home(request):
    featured_products = Product.objects.all()[:3]
    context = {'featured_products': featured_products}
    return render(request, 'products/home.html', context)

def about(request):
    return render(request, 'products/about.html')

def product_list(request):
    search = request.GET.get('search', '')
    products = Product.objects.filter(name__icontains=search)
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

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product was added successfully')
            return redirect('product_list')
    else:
        form = ProductForm()
        return render(request, 'products/product_form.html', {'form':form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} was updated successfully')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
        return render(request, 'products/product_form.html', {'form':form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'{product_name} deleted successfully.')
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product':product})




def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category was added successfully')
            return redirect('category_list')
    else:
        form = CategoryForm()
        return render(request, 'products/category_form.html', {'form':form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'{category.name} was updated successfully')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
        return render(request, 'products/category_form.html', {'form':form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f'{category_name} deleted successfully.')
        return redirect('category_list')
    return render(request, 'products/category_confirm_delete.html', {'category':category})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {'category': category}
    return render(request, 'products/category_detail.html', context)
