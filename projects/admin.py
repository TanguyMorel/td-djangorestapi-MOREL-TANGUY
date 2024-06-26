from django.contrib import admin
from .models import ResearchProject, Researcher, Publication

admin.site.register(ResearchProject)
admin.site.register(Researcher)
admin.site.register(Publication)
