from django.db import models

class Researcher(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ResearchProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project_lead = models.ForeignKey(Researcher, related_name='lead_projects', on_delete=models.CASCADE)
    researchers = models.ManyToManyField(Researcher, related_name='projects')

    def __str__(self):
        return self.title

class Publication(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    project = models.ForeignKey(ResearchProject, related_name='publications', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
