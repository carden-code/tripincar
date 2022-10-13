from django.forms import ModelForm
from django.forms.widgets import DateInput, TimeInput

from .models import Order


class OrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = (
            'city',
            'address',
            'airport',
            'date',
            'time',
            'departure_time',
            'flight_number',
            'telephone',
            'comment',
        )
        widgets = {
            'date': DateInput(attrs={'type': 'date'},
                              format=('%Y-%m-%d'),),
            'time': TimeInput(attrs={'type': 'time'}),
            'departure_time': TimeInput(attrs={'type': 'time'}),
        }
