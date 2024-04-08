from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class PayTaxesForm(forms.Form):
    amount = forms.IntegerField(min_value=1)

class TransferForm(forms.Form):
    account = forms.CharField(min_length=5)
    amount = forms.IntegerField(min_value=0)
