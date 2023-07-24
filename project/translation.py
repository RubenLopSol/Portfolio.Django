from modeltranslation.translator import translator, TranslationOptions
from .models import Project

# Define la traducción para el modelo Project
class ProjectTranslationOptions(TranslationOptions):
    fields = ( 'title_en', 'title_es', 'description_en', 'description_es', )  # Lista de campos que deseas traducir

# Registra la traducción para el modelo Project
translator.register(Project, ProjectTranslationOptions)