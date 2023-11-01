from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import UserCreationForm
from consumer.models import Consumer


class ConsumerSignUpForm(UserCreationForm):
    email = EmailField(help_text='A valid email', required=True)
    class Meta:
        model = Consumer
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(ConsumerSignUpForm, self).save(commit=False)
        user.email = self.clean_data['email']
        if commit:
            user.save()

        return user


class ConsumerSignInForm(ModelForm):
    class Meta:
        model = Consumer
        fields = ['email', 'password']


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Consumer
        fields = ['username', 'email', 'password1', 'password2']
