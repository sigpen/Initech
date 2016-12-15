from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'style': "width: 40%;"}))
    password = forms.CharField(max_length=300, widget=forms.PasswordInput(attrs={'style': "width: 40%;"}))
