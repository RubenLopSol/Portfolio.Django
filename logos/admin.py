from django.contrib import admin
from logos.models import Logos

@admin.register(Logos)
class LogosAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'image']

