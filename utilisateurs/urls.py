# utilisateurs/urls.py

from django.urls import path
from . import views
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]
