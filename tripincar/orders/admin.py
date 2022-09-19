from django.contrib import admin

from .models import Order


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

admin.site.register(Order, OrderAdmin)
