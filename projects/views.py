from django.shortcuts import render
from rest_framework import viewsets
from .models import Researcher, ResearchProject, Publication
from .serializers import ResearcherSerializer, ResearchProjectSerializer, PublicationSerializer

class ResearcherViewSet(viewsets.ModelViewSet):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerializer

class ResearchProjectViewSet(viewsets.ModelViewSet):
    queryset = ResearchProject.objects.all()
    serializer_class = ResearchProjectSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
