from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy


from main.models import Currency
from .forms import RegistrationForm

class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = '/accounts/login/?next=/profile/home/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
