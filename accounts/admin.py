from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import Group
from .models import User
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email','name','is_admin']
    list_filter = ['is_admin']
    fieldsets = [
        (None,{'fields':['name','email','password','last_login']}),
        ("Permissions", {'fields': ['is_active','is_premium','is_admin']})
    ]
    add_fieldsets = (
        (None, {'fields': [ 'email', 'password1', 'password2']}),
    )
    search_fields = ['email','name']
    ordering = ['email']
    filter_horizontal = ()



admin.site.unregister(Group)

admin.site.register(User, UserAdmin)
