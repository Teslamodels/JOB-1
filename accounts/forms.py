from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CreateUser(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'email', 'address']

class ChangeUser(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name']

