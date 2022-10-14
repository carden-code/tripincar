from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.index, name='index'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('order_edit/<int:pk>/', views.order_edit, name='order_edit'),
    path('create/', views.order_create, name='order_create'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_delete/<int:pk>/', views.order_delete, name='order_delete'),

]