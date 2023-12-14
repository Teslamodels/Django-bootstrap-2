from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CreateUser(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'middlename', 'email']

class ChangeUser(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name']