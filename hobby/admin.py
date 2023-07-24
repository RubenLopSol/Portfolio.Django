from django.contrib import admin
from hobby.models import Hobby

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_es', 'description_en', 'description_es', 'image', ]