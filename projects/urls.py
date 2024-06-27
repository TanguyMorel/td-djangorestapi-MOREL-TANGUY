from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResearcherViewSet, ResearchProjectViewSet, PublicationViewSet, home
from . import views

router = DefaultRouter()
router.register(r'researchers', views.ResearcherViewSet)
router.register(r'projects', views.ResearchProjectViewSet)
router.register(r'publications', views.PublicationViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('projects/', views.project_list, name='projects_list'),
    path('publications/', views.publication_list, name='publication_list'),
    path('researchers/', views.researcher_list, name='researchers_list'),
    path('add_researcher/', views.add_researcher, name='add_researcher'),
    path('add_publication/', views.add_publication, name='add_publication'),
     path('add-research-project/', views.add_research_project, name='add_research_project'),
]

