from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Usertype


class Userregister(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": 'نام خود را وارد کنید'}))
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": 'نام خانوادگی خود را وارد کنید'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": 'نام کاربری '}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', "placeholder": 'ایمیل خود را وارد کنید'}))
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": 'رمز عبور خود را وارد کنید'}))
    password2 = forms.CharField(
        label='confirm password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": 'رمزعبور خود را تکرار کنید'}))
    # user_type = forms.ModelChoiceField(
    #     queryset=Usertype.objects.all(),
    #     label='type of user',
    #     empty_label='انتخاب کنید',
    # )

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exist')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this username already exist')
        return username

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError('password most match')


class Userlogin(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": 'نام کاربری خود را وارد کنید'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder": 'رمزعبور خود را وارد کنید'}))