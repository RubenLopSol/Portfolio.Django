from django.contrib import admin
from education.models import Education

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'center', 'year', 'description', 'certificate']

