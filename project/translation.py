from modeltranslation.translator import translator, TranslationOptions
from .models import Project

# Define la traducción para el modelo Project
class ProjectTranslationOptions(TranslationOptions):
    fields = ( 'title', 'description', )  # Lista de campos que deseas traducir

# Registra la traducción para el modelo Project
translator.register(Project, ProjectTranslationOptions)