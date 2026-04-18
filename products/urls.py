from django.urls import path
from .import views
from django.views.defaults import page_not_found


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('about/', views.about, name='about')
]