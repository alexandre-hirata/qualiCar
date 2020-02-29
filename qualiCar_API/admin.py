from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from qualiCar_API import models

admin.site.register (models.Date)


class UserAdmin (BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']

admin.site.register (models.UserProfile, UserAdmin)
