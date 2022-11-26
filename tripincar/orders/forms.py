from django.forms import ModelForm, ValidationError
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
            'departure_date',
            'departure_time',
            'flight_number',
            'telephone',
            'comment',
        )
        widgets = {
            'date': DateInput(attrs={'type': 'date'},
                              format=('%Y-%m-%d'),),
            'time': TimeInput(attrs={'type': 'time'}),
            'departure_date': DateInput(attrs={'type': 'date'},
                                        format=('%Y-%m-%d'),),
            'departure_time': TimeInput(attrs={'type': 'time'}),
        }

    def clean_departure_date(self):
        date = self.cleaned_data.get("date")
        departure_date = self.cleaned_data.get("departure_date")
        if date > departure_date:
            raise ValidationError("Дата подачи не должна быть позже даты вылета!")
        return departure_date

    def clean_departure_time(self):
        departure_time = self.cleaned_data['departure_time']
        time = self.cleaned_data['time']
        departure_date = self.cleaned_data['departure_date']
        date = self.cleaned_data['date']
        if departure_date == date and departure_time <= time:
            raise ValidationError("Время подачи должно быть раньше времени вылета!")
        return departure_time
