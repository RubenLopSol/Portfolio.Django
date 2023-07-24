from django.contrib import admin
from education.models import Education

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_es', 'image', 'center', 'year', 'description_en', 'description_es', 'certificate',]

