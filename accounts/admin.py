from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CreateUser, ChangeUser, CustomUser

class AdminUser(UserAdmin):
    add_form = CreateUser
    form = ChangeUser
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'middle_name', 'email', 'address']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('address', )}),
    )

admin.site.register(CustomUser, AdminUser)