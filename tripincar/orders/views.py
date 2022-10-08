from django.views.generic import ListView
from .models import Order

def index(requesst):
    pass


class OrderListView(ListView):
    queryset = Order.objects.order_by('-pub_date')
    context_object_name = 'order_list'
