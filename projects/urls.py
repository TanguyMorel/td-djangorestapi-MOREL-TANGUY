from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResearcherViewSet, ResearchProjectViewSet, PublicationViewSet, home
from . import views

router = DefaultRouter()
router.register(r'researchers', views.ResearcherViewSet)
router.register(r'projects', views.ResearchProjectViewSet)
router.register(r'publications', views.PublicationViewSet)

urlpatterns = [
    # path('home', views.home, name='home'),
    path('', views.home, name='home'),
    # path('', include(router.urls)), <-----------
    path('projects/', views.project_list, name='projects_list.html'),
    # path('researchers/', views.researcher_list, name='researcher_list'),
    # path('publications/', views.publication_list, name='publication_list'),
]

