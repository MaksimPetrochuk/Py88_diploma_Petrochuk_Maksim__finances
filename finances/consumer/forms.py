from django.forms import ModelForm, TextInput, EmailField
from django.contrib.auth.forms import UserCreationForm
from consumer.models import Consumer

class ConsumerSignUpForm(ModelForm):
    class Meta:
        model = Consumer
        fields = ['username', 'email', 'password']


class ConsumerSignInForm(ModelForm):
    class Meta:
        model = Consumer
        fields = ['email', 'password']