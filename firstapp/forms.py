from django import forms

class HouseForm(forms.Form):
    address = forms.CharField(label='Адресс')
    year = forms.IntegerField(label='Год постройки')
