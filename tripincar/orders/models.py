from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Заказчик',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    
    address = models.CharField(
        verbose_name='Адрес',
        max_length=256,
        blank=False
    )
    
    telephone = models.CharField(
        verbose_name='Телефон',
        max_length=11,
        unique=True,
        blank=False
    )

    comment = models.CharField(
        verbose_name='Комментарий',
        max_length=256,
        blank=True
    )
