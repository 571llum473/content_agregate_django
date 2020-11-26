from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """Custom UserCreationForm(new email field)"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Придумайте логин'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите почту'
        self.fields['password1'].widget.attrs['placeholder'] = 'Придумайте пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

class ChangeProfileForm(forms.ModelForm):
    """Change password in user model"""
    class Meta:
        model = User
        fields = ['username', 'email']
