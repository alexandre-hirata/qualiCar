from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from qualiCar_API import models
from qualiCar_API.models import Part

admin.site.register (models.Date)


class UserAdmin (BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login', )})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1','password2')
        }),
    )

class PartAdmin (ImportExportModelAdmin):
    pass

# These lines adds models to admin page
admin.site.register (models.UserProfile, UserAdmin)
admin.site.register (models.Part, PartAdmin)
admin.site.register (models.Vehicle)
admin.site.register (models.Incident)
