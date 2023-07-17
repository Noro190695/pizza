from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField(label='Full name', max_length=100)
    phone = forms.IntegerField(label='Phone')
    email = forms.EmailField(label='E-mail')
    address = forms.CharField(label='Address')
