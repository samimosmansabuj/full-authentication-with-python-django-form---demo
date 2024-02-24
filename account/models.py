from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    is_varified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.username} | {self.email}'


