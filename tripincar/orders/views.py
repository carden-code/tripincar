from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import OrderForm
from .models import Order

User = get_user_model()

def index(request):
    return render(request, template_name='orders/index.html')

@login_required
def order_list(request):
    orders = Order.objects.order_by('-pub_date')
    template = 'orders/order_list.html'
    context = {
        'orders': orders,
    }
    return render(request, template_name=template, context=context)

@login_required
def order_detail(request, pk):
    """Обработчик страницы заказа в деталях."""
    order = get_object_or_404(Order, id=pk)
    form_order = OrderForm(instance=order)
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
def order_create_in_airport(request):
    """Обработчик создания заказа."""
    template = 'orders/create_order.html'
    phone = request.user.telephone
    initial_dict = {
        "telephone": phone
    }
    
    form = OrderForm(
        request.POST or None,
        initial=initial_dict
    )

    if form.is_valid():
        order = form.save(commit=False)
        order.author = request.user
        if not order.telephone:
            order.telephone = request.user.telephone
        order.save()
        return redirect('orders:order_detail', order.pk)

    context = {
        'form': form
    }
    return render(request, template_name=template, context=context)

@login_required
def order_create_in_city(request):
    """Обработчик создания заказа."""
    template = 'orders/create_order.html'
    phone = request.user.telephone
    initial_dict = {
        "telephone": phone
    }
    
    form = OrderForm(
        request.POST or None,
        initial=initial_dict
    )

    if form.is_valid():
        order = form.save(commit=False)
        order.author = request.user
        if not order.telephone:
            order.telephone = request.user.telephone
        order.save()
        return redirect('orders:order_detail', order.pk)

    context = {
        'form': form
    }
    return render(request, template_name=template, context=context)

@login_required
def order_edit(request, pk):
    """Обработчик редактирования заказа."""
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

@login_required
def order_delete(request, pk):
    user_name = request.user.username
    order = get_object_or_404(Order, id=pk)
    order.delete()
    return redirect('users:profile', user_name)
