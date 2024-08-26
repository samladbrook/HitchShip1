# jobs/forms.py
from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'pickup_location',
            'destination',
            'item_name',
            'quantity',
            'total_weight',
            'SKU',
            'description',
        ]
        labels = {
            'item_name': 'Item Name',
            'total_weight': 'Total Weight',
        }
        widgets = {
            'pickup_location': forms.TextInput(attrs={'id': 'starting-point', 'placeholder': 'Enter starting point'}),
            'destination': forms.TextInput(attrs={'id': 'destination', 'placeholder': 'Enter destination'}),
        }
        

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        job = super().save(commit=False)
        if self.user:
            job.added_by = self.user
        if commit:
            job.save()
        return job