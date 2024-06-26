# projects/forms.py
from django import forms
from .models import Researcher, Publication

class ResearcherForm(forms.ModelForm):
    class Meta:
        model = Researcher
        fields = ['name', 'specialty']
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'summary', 'project', 'publication_date']