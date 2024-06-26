# projects/forms.py
from django import forms
from .models import Researcher

class ResearcherForm(forms.ModelForm):
    class Meta:
        model = Researcher
        fields = ['name', 'specialty']