from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)