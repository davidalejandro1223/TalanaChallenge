from django import forms

class SetPasswordForm(forms.Form):
    password = forms.CharField(label='Ingresa tu contraseña', widget=forms.PasswordInput)
