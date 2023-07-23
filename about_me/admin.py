from django.contrib import admin
from about_me.models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass





