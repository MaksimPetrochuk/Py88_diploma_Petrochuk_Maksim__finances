from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy

from .forms import SettingsForm, CreateCostGroupForm, CreateCostRecordForm


@login_required
def profile(request):
    return render(request, 'consumer_profile/profile.html')

class SettingsView(FormView):
    form_class = SettingsForm
    template_name = 'consumer_profile/settings.html'
    success_url = reverse_lazy('consumer_profile:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CreateCostGroupView(FormView):
    form_class = CreateCostGroupForm
    template_name = 'consumer_profile/create_cost_group.html'
    success_url = reverse_lazy('consumer_profile:home')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CreateCostRecordView(FormView):
    form_class = CreateCostGroupForm
    template_name = 'consumer_profile/create_cost_record.html'
    success_url = reverse_lazy('consumer_profile:home')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)