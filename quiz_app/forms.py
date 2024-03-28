from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError


class MinLengthValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError(f"Password must be at least {self.min_length} characters long.")


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Login'

    }))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'

    }))




# Форма для регистрации
class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }),
        validators=[MinLengthValidator()])

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm the password'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Login'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last name'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


# Форма для зименения Даных аккаунта
class EditAccountForm(UserChangeForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


# Форма для зименения Даных профиля
class EditProfileForm(forms.ModelForm):
    photo = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Profile
        fields = ['photo', 'phone_number']
