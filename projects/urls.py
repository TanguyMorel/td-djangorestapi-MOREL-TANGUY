from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResearcherViewSet, ResearchProjectViewSet, PublicationViewSet, home
from . import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'researchers', views.ResearcherViewSet)
router.register(r'projects', views.ResearchProjectViewSet)
router.register(r'publications', views.PublicationViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('projects/', views.project_list, name='projects_list'),
     path('publications/', views.publication_list, name='publication_list'),
    path('publications/delete/<int:publication_id>/', views.delete_publication, name='delete_publication'),
    path('researchers/', views.researcher_list, name='researchers_list'),
    path('add_researcher/', views.add_researcher, name='add_researcher'),
    path('researchers/delete/<int:researcher_id>/', views.delete_researcher, name='delete_researcher'),
    path('add_publication/', views.add_publication, name='add_publication'),
    path('add-research-project/', views.add_research_project, name='add_research_project'),
    path('delete-project/<int:pk>/', views.delete_project, name='delete_project'),
    path('admin/', admin.site.urls),
    path('', include('utilisateurs.urls')),
]

