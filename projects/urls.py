from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResearcherViewSet, ResearchProjectViewSet, PublicationViewSet, home

router = DefaultRouter()
router.register(r'researchers', ResearcherViewSet)
router.register(r'projects', ResearchProjectViewSet)
router.register(r'publications', PublicationViewSet)

urlpatterns = [
    path('', home, name='home'), 
    path('', include(router.urls)),
]

