from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('add/', views.cart_add, name='cart_add'),
    path('delet/', views.cart_delet, name='cart_delet'),
    path('update/', views.cart_update, name='cart_update'),
]


