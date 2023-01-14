from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Airport, City, Favorite, Order, Route

User = get_user_model()


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


class AirportAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


class RouteAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'city',
        'airport',
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'telephone',
        'pub_date',
        'update_date',
        'route',
        'driver',
        'status',
    )
    search_fields = ('pub_date',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'driver', 'order')
 

admin.site.register(Airport, AirportAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Favorite, FavoriteAdmin)
