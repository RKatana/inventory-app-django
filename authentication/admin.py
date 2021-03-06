from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

User = get_user_model()

# Register your models here.
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None,{"fields": ('email', 'password', 'name', 'last_login',)}),
        ('Permissions', {"fields":(
            'is_active',
            'groups',
            'user_permissions'
        )}),
    )

    add_fieldsets = (
        (
            None,
            {'classes':('wide',),
            'fields': ('email', 'password1', 'password2',)
            }
        ),
    )

    list_display = ('email', 'name', 'role', 'last_login',)
    list_filter = ('is_active', 'groups',)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(get_user_model(),UserAdmin)
admin.site.register(Profile)
admin.site.site_header='Inventory Stock Admin'

