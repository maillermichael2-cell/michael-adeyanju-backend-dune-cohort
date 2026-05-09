from django.urls import path
from .import views 
from .views import product_list_json, product_detail_json 
from .views import ProductListAPIView, ProductDetailAPIView, CategoryListAPIView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('404/', views.page_not_found,{'exception': Exception('Page not found!')}),
    path('products/add/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/',views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('categories/add/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/',views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),



    # JSON VIEWS URLS 
    path('api/products/json/', product_list_json, name='product-list-json'),
    path('api/products/json/<int:pk>/', product_detail_json, name='product-detail-json'),


    # LIST ALL PRODUCTS
    path('api/products/',ProductListAPIView.as_view(), name='api-product-list' ),
    path('api/products/<int:pk>/',ProductDetailAPIView.as_view(), name='api-product-detail' ),

    #LIST ALL CATEGORIES
    path('api/categories/', CategoryListAPIView.as_view(), name='api-category-list'),
]