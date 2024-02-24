from django import forms
from .models import Custom_User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


class UserRegistrationForm(UserCreationForm):
    USER_TYPE = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Phone Number', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email Address', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    user_type = forms.CharField(label='User Type', max_length=20, widget=forms.Select(choices=USER_TYPE, attrs={'class': 'form-control'}))
    
    class Meta:
        model = Custom_User
        fields = ['first_name', 'username', 'phone_number', 'email', 'user_type']



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='New Confirm Passowrd', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ForgetPassword(forms.Form):
    email = forms.EmailField(max_length=50, label='Email Address', widget=forms.EmailInput(attrs={'class': 'form-control'}))


class ResetPasswordForm(forms.Form):
    otp = forms.CharField(max_length=6, label='OTP', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='New Confirm Passowrd', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

class RegistrationVerificationForm(forms.Form):
    otp = forms.CharField(max_length=6, label='OTP', widget=forms.NumberInput(attrs={'class': 'form-control'}))

