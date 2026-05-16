from django.shortcuts import render,get_object_or_404, redirect
from .models import Product, Category
from django.db.models import Count
from django.http import HttpResponse
from django.contrib import messages
from .forms import ProductForm, CategoryForm
from django.contrib.auth.decorators import login_required
# new import
import json
from django.http import JsonResponse
# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, CategorySerializer
# 
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .pagination import ProductPagination
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly



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

@login_required
def product_create(request):
    if not request.user.is_staff:
        messages.error(request, 'You are not authorized to create products')
        return redirect('product_list')
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product was added successfully')
            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, 'products/product_form.html', {'form':form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if not request.user.is_staff:
        messages.error(request, 'You are not authorized to update this product')
        return redirect('product_list')
    
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} was updated successfully')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/product_form.html', {'form':form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if not request.user.is_staff:
        messages.error(request, 'You are not authorized to delete this product')
        return redirect('product_list')
    
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'{product_name} deleted successfully')
        return redirect('product_list')
    
    return render(request, 'products/product_confirm_delete.html', {'product': product})


@login_required
def category_create(request):
    if not request.user.is_staff:
        messages.error(request, 'You are not authorized to create category')
        return redirect('category_list')
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category was added successfully')
            return redirect('category_list')
    else:
        form = CategoryForm()
        
    return render(request, 'products/category_form.html', {'form':form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if not request.user.is_staff:
        messages.error(request, 'You are not authorized to  update category ')
        return redirect('category_list')
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'{category.name} was updated successfully')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
        
    return render(request, 'products/category_form.html', {'form':form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if not request.user.is_staff:
        messages.error(request, 'You are not authorized to delete this category')
        return redirect('category_list')

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






# JSON VIEWS FORM PRODUCT LIST AND PRODUCT DETAIL JSON

def product_list_json(request):
    products = Product.objects.all()
    data = [
        {
            "id": p.id,
            "name": p.name,
            "price": str(p.price),
            "stock": p.stock,
            "is_available": p.is_available,
        }for p in products
    ]
    return JsonResponse(data, safe=False)

def product_detail_json(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "stock":product.stock,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        error = {'error': 'Product Not Found'}
        return JsonResponse(error, status=404)



# lis all products  and add new product
class ProductListAPIView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter ]
    filterset_fields = ["category", "is_available"]
    search_fields = ["name", "category__name"]
    ordering_fields = ["price","created_at","stock"]
    ordering = ["-created_at"]

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        filtered_queryset = self.filter_queryset(self.queryset)
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(filtered_queryset, request, view=self )

        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try: 
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None
    
    def get(self, request, pk):
        product = self.get_object(pk)

        if product is None:
            return Response(
                {'error': 'Not Found'},
                status = status.HTTP_404_NOT_FOUND
            )
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({'error': 'Product Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):
        product = self.get_object(pk)

        if product is None:
            return Response(
                {'error': 'Not Found'},
                status = status.HTTP_404_NOT_FOUND
            )
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListAPIView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    


# new product create view 

class ProductCreateApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)