from django.contrib import admin
from data.models import Data

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'image', 'position_en', 'position_es', 'gitHub', 'linkedin', 'cv', 'updated']

