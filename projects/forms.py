# projects/forms.py
from django import forms
from .models import Researcher, Publication, ResearchProject

class ResearcherForm(forms.ModelForm):
    class Meta:
        model = Researcher
        fields = ['name', 'specialty']
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'summary', 'project', 'publication_date']

class ResearchProjectForm(forms.ModelForm):
    class Meta:
        model = ResearchProject
        fields = ['title', 'description', 'start_date', 'end_date', 'project_lead', 'researchers']
        widgets = {
            'researchers': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project_lead'].queryset = Researcher.objects.all()
        self.fields['researchers'].queryset = Researcher.objects.all()