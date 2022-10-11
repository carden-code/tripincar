from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Order
from .forms import OrderForm

User = get_user_model()


def index(request):
    return render(request, template_name='orders/index.html')

def order_list(request):
    orders = Order.objects.order_by('-pub_date')
    template = 'orders/order_list.html'
    context = {
        'orders': orders,
    }
    return render(request, template_name=template, context=context)


def order_detail(request, pk):
    """Обработчик страницы заказа в деталях."""
    order = get_object_or_404(Order, id=pk)
    form_order = OrderForm()
    user = order.author
    count_orders = user.orders.count()
    template = 'orders/order_detail.html'
    context = {
        'order': order,
        'count_orders': count_orders,
        'form': form_order,
    }
    return render(request, template_name=template, context=context)


@login_required
def order_create(request):
    """Обработчик создания поста."""
    template = 'orders/create_order.html'
    form = OrderForm(
        request.POST or None,
    )

    if form.is_valid():
        order = form.save(commit=False)
        order.author = request.user
        order.save()
        return redirect(template='orders:index')

    context = {
        'form': form
    }
    return render(request, template_name=template, context=context)


@login_required
def order_edit(request, pk):
    """Обработчик редактирования поста."""
    order = get_object_or_404(Order, id=pk)

    form = OrderForm(
        request.POST or None,
        instance=order
    )
    if form.is_valid() and order.author == request.user:
        form.save()
        return redirect('orders:order_detail', order.pk)

    template = 'orders/create_order.html'
    context = {
        'form': form,
    }
    return render(request, template_name=template, context=context)
    


# class OrderListView(ListView):
#     queryset = Order.objects.order_by('-pub_date')
#     context_object_name = 'order_list'
