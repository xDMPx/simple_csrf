from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class WithdrawForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
