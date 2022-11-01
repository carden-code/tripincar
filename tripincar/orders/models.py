from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


# class Price(models.Model):
#     price = models.IntegerField(
#         verbose_name='Стоимость',
#         blank=True,
#         validators=[
#             MinValueValidator(3000),
#         ]
#     )
        
#     def __str__(self):
#         return f'Стоимость: {self.price}'


class Airport(models.Model):
    name = models.CharField(
        verbose_name='Аэропорт',
        max_length=128,
    )

    start_price = models.IntegerField(
        verbose_name='Стартовая стоимость',
    )
        

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
    
    departure_time = models.TimeField(
        verbose_name='Время вылета',
        auto_now=False,
        auto_now_add=False,
        null=False
    )
    
    telephone = models.CharField(
        verbose_name='Телефон',
        max_length=11,
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

