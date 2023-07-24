from django.contrib import admin
from work.models import Work

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'year', 'description_en', 'description_es', 'logo',]

