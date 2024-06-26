from django.shortcuts import render
from rest_framework import viewsets
from .models import Researcher, ResearchProject, Publication
from .serializers import ResearcherSerializer, ResearchProjectSerializer, PublicationSerializer
from django.http import HttpResponse


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

# def home(request):

#         # home = ResearchProject.objects.all()
#         # return render(request, 'home.html', {'projects': home})
#     return HttpResponse("Bienvenue sur la page d'accueil des projets de recherche!")

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
