# Generated by Django 5.0.6 on 2024-06-26 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('project_lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_projects', to='projects.researcher')),
                ('researchers', models.ManyToManyField(related_name='projects', to='projects.researcher')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('publication_date', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='projects.researchproject')),
            ],
        ),
    ]