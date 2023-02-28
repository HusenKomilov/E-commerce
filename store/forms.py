from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Foydalanuvchi ismi"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        'placeholder': "Parol"
    }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "Parol"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "Tasdiqlash"
    }))

    class Meta:
        model = User
        fields = ("username", 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Foydalanuvchi ismi"
            }),
            "email": forms.EmailInput(attrs={
                "class": 'form-control',
                'placeholder': 'Email'
            })
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
        widgets = {
            "text": forms.Textarea(attrs={
                'placeholder': "Komentariya...",
                'class': "form-control"
            })
        }


class CustomerForms(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ismingiz ..."
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Familiyangiz ...'
            })
        }


class ShippingForms(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('address', 'city', 'state', 'phone')
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Address ..."
            }),
            'city': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': "City ..."
            }),
            'state': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Ko'cha ..."
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Telefon nomer ..."
            })
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
