from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    
    path('change-password/', change_password, name='change_password'),
    
    path('forget-password/', forget_password, name='forget_password'),
    path('reset-password/', reset_password, name='reset_password'),
    
]