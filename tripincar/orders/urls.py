from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders_list),
    path('order/<int:pk>/', views.order_detail),
]