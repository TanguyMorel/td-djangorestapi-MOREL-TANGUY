from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Researcher, ResearchProject, Publication
from .serializers import ResearcherSerializer, ResearchProjectSerializer, PublicationSerializer
from django.http import HttpResponse
from .forms import ResearcherForm, PublicationForm, ResearchProjectForm


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
    # Récupérer tous les chercheurs
    researchers = Researcher.objects.all()

    # Si la méthode de requête est POST, traiter le formulaire
    if request.method == 'POST':
        form = ResearchProjectForm(request.POST)
        if form.is_valid():
            # Enregistrer le projet de recherche
            project_instance = form.save()
            print("Projet sauvegardé avec succès:", project_instance)
            return redirect('home')  # Rediriger vers la même page après soumission
        else:
            print("Erreurs de validation:", form.errors)
    else:
        form = ResearchProjectForm()

    # Passer le formulaire et les chercheurs au contexte de la page d'accueil
    context = {
        'form': form,
        'researchers': researchers,
    }
    return render(request, 'projects/home.html', context)

def add_researcher(request):
    if request.method == 'POST':
        form = ResearcherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirection après ajout réussi
    else:
        form = ResearcherForm()
        

def add_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirection vers la page d'accueil ou toute autre page après l'ajout réussi
    else:
        form = PublicationForm()
    
def add_research_project(request):
    if request.method == 'POST':
        form = ResearchProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ResearchProjectForm()

    return render(request, 'projects/home.html', {'form': form})


def project_list(request):
    projects = ResearchProject.objects.all()
    return render(request, 'projects/projects_list.html', {'projects': projects})
    # return HttpResponse("Yopdilp")


def researcher_list(request):
    researchers = Researcher.objects.all()
    context = {
        'researchers': researchers,
    }
    return render(request, 'projects/researchers_list.html', context)

def delete_researcher(request, researcher_id):
    researcher = get_object_or_404(Researcher, id=researcher_id)
    if request.method == 'POST':
        researcher.delete()
        return redirect('researchers_list')
    # Si la méthode est GET, afficher une page de confirmation de suppression ou rediriger vers la liste des chercheurs
    return redirect('researchers_list')  # Redirection par défaut

def publication_list(request):
    publications = Publication.objects.all()
    context = {
        'publications': publications,
    }
    return render(request, 'projects/publication_list.html', context)

def delete_publication(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    if request.method == 'POST':
        publication.delete()
        return redirect('publication_list')
    # Si la méthode est GET, afficher une page de confirmation de suppression ou rediriger vers la liste des publications
    return redirect('publication_list')  # Redirection par défaut

def delete_project(request, pk):
    project = get_object_or_404(ResearchProject, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects_list')  # Redirection vers la liste des projets après suppression
    else:
        # Affichage d'une confirmation de suppression (optionnel)
        context = {
            'project': project,
        }
        return render(request, 'delete_project.html', context)
