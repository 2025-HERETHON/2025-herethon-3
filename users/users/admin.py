from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['user_id', 'name', 'email']
    fieldsets = (
        (None, {'fields': ('user_id', 'name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('user_id', 'name', 'email', 'password1', 'password2'),
        }),
    )
    ordering = ('user_id',)

admin.site.register(CustomUser, CustomUserAdmin)

