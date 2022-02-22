from django.urls import path
from .views import HomeView , CategoryView, TestView, ProductView, ProductCatView, CartView, ThongTinView, OrderView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name = 'indext'),
    path('indext', HomeView.as_view(), name = 'indext'),
    path('category', CategoryView.as_view(), name = 'category'),
    path('productcat<int:id>', ProductCatView.as_view(), name = 'productcat'),
    path('product<int:id>', ProductView.as_view(), name = 'product'),
    path('tt', ThongTinView.as_view(), name = 'thongtin'),
    path('cart', CartView.as_view(), name = 'carts'),
    path('order', OrderView.as_view(), name = 'order'),


    path('Cart/addcart', views.addcart, name ='cart'),

    path('test', TestView.as_view(), name = 'test'),

]
