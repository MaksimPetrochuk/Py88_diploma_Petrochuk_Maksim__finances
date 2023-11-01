from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import UserCreationForm
from consumer.models import Consumer


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Consumer
        fields = ['username', 'email', 'password1', 'password2']
