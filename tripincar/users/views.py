from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render

# Импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('orders:index')
    template_name = 'users/signup.html'


def profile(request, username):
    """Обработчик страницы автора."""
    author = get_object_or_404(User, username=username)
    orders = author.orders.all()

    template = 'users/profile.html'
    context = {
        'orders_user': orders,
        'username': author,
    }
    return render(request, template_name=template, context=context)