from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + ((None,{"fields":("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{"fields":("name",)}),)
    # add_fieldsets in admin → tells Django how to render and group those fields on the admin page.
    # specifies what fields to be displayed in the admin panel
    # Note that in usercreation or useredit

admin.site.register(CustomUser,CustomUserAdmin)

