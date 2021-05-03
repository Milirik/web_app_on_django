from django import forms

from .models import User, Attributes


class AuthUser(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1')


class AttributesForm(forms.ModelForm):
    class Meta:
        model = Attributes
        fields = '__all__'
