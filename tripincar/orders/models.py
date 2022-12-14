from django.db import models
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class Airport(models.Model):
    name = models.CharField(
        verbose_name='Аэропорт',
        max_length=128,
    )

    start_price = models.IntegerField(
        verbose_name='Стартовая стоимость',
    )
    
    class Meta:
        verbose_name = 'Аэропорт'
        verbose_name_plural = 'Аэропорты'
    
    def __str__(self):
        return f'{self.name}'
        

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
    
    number = models.IntegerField(
        verbose_name='Номер',
        default=0
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
    
    airport = models.ForeignKey(
        Airport,
        verbose_name='Аэропорт',
        on_delete=models.SET_NULL,
        null=True
    )
    
    flight_number = models.CharField(
        verbose_name='Номер рейса',
        max_length=16
    )
    
    date = models.DateField(
        verbose_name='Дата подачи авто',
    )
    
    time = models.TimeField(
        verbose_name='Время подачи авто',
        auto_now=False,
        auto_now_add=False,
        null=False
    )
    
    departure_date = models.DateField(
        verbose_name='Дата вылета',
        auto_now=False,
        auto_now_add=False,
        null=False
    )
    
    departure_time = models.TimeField(
        verbose_name='Время вылета',
        auto_now=False,
        auto_now_add=False,
        null=False,
    )
    
    telephone = PhoneNumberField(
        verbose_name='Телефон',
        blank=True, 
        region='RU'
    )

    comment = models.TextField(
        verbose_name='Комментарий',
        max_length=256,
        blank=True
    )
    
    price = models.IntegerField(
        verbose_name='Стоимость',
        blank=True,
        null=True
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
    
    def counter():
        
        pass


class Favorite(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name='Заказ',
        on_delete=models.CASCADE,
    )
    driver = models.ForeignKey(
        User,
        verbose_name='Водитель',
        on_delete=models.CASCADE,
    )
    
    class Meta:
        verbose_name = 'Принятый заказ'
        verbose_name_plural = 'Принятые заказы'
        
    def __str__(self):
        return f'{self.driver} - {self.order}'

