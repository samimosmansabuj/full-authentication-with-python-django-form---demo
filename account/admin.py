from django.contrib import admin
from .models import Custom_User


@admin.register(Custom_User)
class Custom_UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_varified', 'user_type']
    list_filter = ['user_type']
    search_fields = ['username', 'email']
