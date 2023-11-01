from django.forms import ModelForm
from consumer.models import Consumer, CostGroup, CostRecord


class SettingsForm(ModelForm):
    class Meta:
        model = Consumer
        fields = ['default_currency']

    def save(self, commit=True):
        user = super(SettingsForm, self).save(commit=False)
        user.default_currency = self.clean_data['default_currency']
        if commit:
            user.save()

class CreateCostGroupForm(ModelForm):
    class Meta:
        model = CostGroup
        fields = ['cost_group_name']

    def save(self, commit=True):
        group = super(CreateCostGroupForm, self).save(commit=False)
        group.cost_group_name = self.clean_data['cost_group_name']
        if commit:
            group.save()

class CreateCostRecordForm(ModelForm):
    class Meta:
        model = CostRecord
        fields = ['cost_group', 'cost', 'currency', 'time']

    def save(self, commit=True):
        record = super(CreateCostRecordView, self).save(commit=False)
        record.default_currency = self.clean_data['default_currency']
        if commit:
            record.save()

