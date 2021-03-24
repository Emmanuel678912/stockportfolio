from django import forms
from .models import Stock

class StockForm(forms.ModelForm): # create a form that collects data that can be sent to a database
    class Meta:
        model = Stock 
        fields = ['ticker'] # data you want to collect 