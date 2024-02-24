from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, UserPasswordChangeForm, ForgetPassword, ResetPasswordForm
from django.contrib.auth import login, update_session_auth_hash, logout
from django.core.mail import send_mail
from django.conf import settings
from .models import Custom_User
import random


def registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'account/registration.html', {'form': form})

def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'account/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'home.html')


def change_password(request):
    form = UserPasswordChangeForm(request.user)
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'account/change_password.html', {'form': form})


def forget_password(request):
    form = ForgetPassword()
    if request.method == 'POST':
        form = ForgetPassword(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Custom_User.objects.filter(email=email).exists():
                otp = random.randint(111111, 999999)
                user = Custom_User.objects.get(email=email)
                request.session['forget_password_otp'] = otp
                request.session['forget_password_email'] = email
                
                subject = "Forget Passwod OTP!"
                body = f"""Dear User, 
                Your Mail {email}: 
                Your OTP {otp}"""
                sender = settings.EMAIL_HOST_USER
                receiver = [email]
                send_mail(subject=subject, message=body, from_email=sender, recipient_list=receiver)
                return redirect('reset_password')
                
    return render(request, 'account/forget_password.html', {'form': form})

from django.contrib import messages

def reset_password(request):
    form = ResetPasswordForm()
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            otp = int(form.cleaned_data.get('otp'))
            new_password1 = form.cleaned_data.get('new_password1')
            new_password2 = form.cleaned_data.get('new_password2')
            
            stored_otp = request.session.get('forget_password_otp')
            stored_email = request.session.get('forget_password_email')
            
            print('otp type', type(otp))
            print('stored otp type', type(stored_otp))
            
            if otp == stored_otp:
                if new_password1 == new_password2:
                    user = Custom_User.objects.get(email=stored_email)
                    user.set_password(new_password1)
                    user.save()
                    messages.success(request, "Password Reset!")
                    return redirect('login')
                else:
                    messages.warning(request, "New Password & Confirm Password Doesn't Match!!")
            else:
                messages.warning(request, "OTP Doesn't Match!")
            
    return render(request, 'account/reset_password.html', {'form': form})


