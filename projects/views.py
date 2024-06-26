from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import Researcher, ResearchProject, Publication
from .serializers import ResearcherSerializer, ResearchProjectSerializer, PublicationSerializer
from django.http import HttpResponse
from .forms import ResearcherForm


# ViewSets pour l'API REST
class ResearcherViewSet(viewsets.ModelViewSet):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerializer

class ResearchProjectViewSet(viewsets.ModelViewSet):
    queryset = ResearchProject.objects.all()
    serializer_class = ResearchProjectSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

# Views pour le front


def home(request):
    return render(request, 'projects/home.html')

def add_researcher(request):
    if request.method == 'POST':
        form = ResearcherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirection après ajout réussi
    else:
        form = ResearcherForm()


def project_list(request):
    projects = ResearchProject.objects.all()
    return render(request, 'projects/projects_list.html', {'projects': projects})
    # return HttpResponse("Yopdilp")


def researcher_list(request):
    researchers = Researcher.objects.all()
    return render(request, 'projects/researcher_list.html', {'researchers': researchers})

def publication_list(request):
    publications = Publication.objects.all()
    return render(request, 'projects/publication_list.html', {'publications': publications})
