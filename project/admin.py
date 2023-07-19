from django.contrib import admin
from project.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'description', 'deployment', 'code_front', 'code_back']