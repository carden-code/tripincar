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
            'telephone',
            'comment',
        )
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'}),
        }
