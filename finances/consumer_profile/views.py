from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy

from .forms import SettingsForm


@login_required
def profile(request):
    return render(request, 'consumer_profile/profile.html')

class SettingsView(FormView):
    form_class = SettingsForm
    template_name = 'consumer_profile/settings.html'
    success_url = 'profile'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CreateCostGroupView(FormView):
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CreateCostRecordView(FormView):
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)