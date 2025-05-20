from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# UserCreationForm.fields (in the form's Meta) controls which fields are in the form logic — i.e., which fields will be validated, shown, and saved.

# UserAdmin.add_fieldsets only controls the layout of the admin panel — it does not automatically include fields in the form.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # UserCreationForm is for creating a new user — so it keeps things minimal.
        # thus contains only username,password1,password2 field and we have also added name there
        fields = UserCreationForm.Meta.fields + ("name",)


# Why do I see first_name, last_name, etc. in admin?	Because your model inherits from AbstractUser, and you're using UserChangeForm which includes those fields.
# this cludes first_name, last_name, email, etc. — because they are part of Django’s built-in AbstractUser mode
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

# UserCreationForm	It uses a limited set of fields (username, password1, password2) — so you must extend it to include custom ones like "name".
# UserChangeForm	It already includes all model fields — so "name" is automatically there if it exists in your model.