from django.db import models
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class City(models.Model):
    name = models.CharField(
        verbose_name='Город',
        max_length=128,
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class Airport(models.Model):
    name = models.CharField(
        verbose_name='Аэропорт',
        max_length=128,
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Аэропорт'
        verbose_name_plural = 'Аэропорты'
    
    def __str__(self):
        return f'{self.name}'


class Route(models.Model):
    city = models.ForeignKey(
        City,
        verbose_name='Город',
        related_name='routes',
        on_delete=models.SET_NULL,
        null=True
    )
    airport = models.ForeignKey(
        Airport,
        verbose_name='Аэропорт',
        related_name='routes',
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
    
    def __str__(self):
        return f'{self.city} - {self.airport}'
    
    
class Order(models.Model):
    
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
    
    route = models.ForeignKey(
        Route,
        verbose_name='Маршрут',
        on_delete=models.SET_NULL,
        null=True
    )
    
    address = models.CharField(
        verbose_name='Адрес',
        max_length=256,
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
        return f'{self.route}'
    
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

