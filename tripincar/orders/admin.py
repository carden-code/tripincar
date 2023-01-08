from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Airport, Favorite, Order

User = get_user_model()


class AirportAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'start_price',
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'telephone',
        'pub_date',
        'update_date',
        'city',
        'airport',
        'driver',
        'status',
    )
    search_fields = ('airport',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'driver', 'order')
 

admin.site.register(Order, OrderAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Favorite, FavoriteAdmin)
