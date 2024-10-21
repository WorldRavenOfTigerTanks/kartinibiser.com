from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['year_in_school','year_in_school2','city' ,'postal_code','first_name', 'last_name', 'email', 'postal_code2' ,'address', 'city2' ]