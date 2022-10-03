from django.shortcuts import render, redirect

from orders.forms import OrderForm


def index(request):
    return render(request, template_name='posts/index.html')

def order_create(request):
    """Обработчик создания заказа."""
    template = 'orders/create_order.html'
    form = OrderForm(
        request.POST or None,
        files=request.FILES or None
    )

    if form.is_valid():
        order = form.save(commit=False)
        order.author = request.user
        order.save()
        return redirect('orders:index')

    context = {
        'form': form
    }
    return render(request, template_name=template, context=context)
