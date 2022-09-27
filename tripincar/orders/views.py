from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, template_name='posts/index.html')

def orders_list(request):
    return HttpResponse('Список заказов')

def order_detail(request, pk):
    return HttpResponse(f'Заказ {pk}')
