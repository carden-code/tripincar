from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('orders/', views.orders_list),
    path('order/<int:pk>/', views.order_detail),
]