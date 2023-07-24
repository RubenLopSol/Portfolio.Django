from django.contrib import admin
from project.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_es', 'image', 'description_en', 'description_es', 'deployment', 'code_front', 'code_back']
