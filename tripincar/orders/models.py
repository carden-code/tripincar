from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
    

class Order(models.Model):
    
    CITY_CHOICES = (
        ('Рязань', 'Рязань'),
        ('Тула', 'Тула'),
        ('Владимир', 'Владимир'),
    )
    
    AIRPORT_CHOICES = (
        ('Домодедово', 'Домодедово'),
        ('Внуково', 'Внуково'),
        ('Шереметьево', 'Шереметьево'),
        ('Жуковский', 'Жуковский'),
    )

    author = models.ForeignKey(
        User,
        verbose_name='Заказчик',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    
    driver = models.ForeignKey(
        User,
        verbose_name='Водитель',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    city = models.CharField(
        verbose_name='Город',
        max_length=128,
        choices=CITY_CHOICES,
        default='',
    )
    
    address = models.CharField(
        verbose_name='Адрес',
        max_length=256,
    )
    
    airport = models.CharField(
        verbose_name='Аэропорт',
        max_length=64,
        choices=AIRPORT_CHOICES,
        default='',
    )
    
    date = models.DateField(
        verbose_name='Дата подачи авто',
        null=False
    )
    
    time = models.TimeField(
        verbose_name='Время подачи авто',
        auto_now=False,
        auto_now_add=False,
        null=False
    )
    
    telephone = models.CharField(
        verbose_name='Телефон',
        max_length=11,
    )

    comment = models.CharField(
        verbose_name='Комментарий',
        max_length=256,
        blank=True
    )
    
    status = models.BooleanField(
        verbose_name='Статус заказа',
        default=False
    )
    
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True
    )
    
    update_date = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-pub_date',)
        
    def __str__(self):
        return f'{self.airport} -> {self.city}'
