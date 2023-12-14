from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import CreateUser, ChangeUser, CustomUser

class Admin(UserAdmin):
    add_form = CreateUser
    form = ChangeUser
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'middlename', 'email']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('middlename', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('middlename', )}),
    )

admin.site.register(CustomUser, Admin)