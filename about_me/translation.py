from modeltranslation.translator import translator, TranslationOptions
from .models import About

# Define la traducción para el modelo About
class AboutTranslationOptions(TranslationOptions):
    fields = ('description_en', 'description_es',)  # Lista de campos que deseas traducir

# Registra la traducción para el modelo About
translator.register(About, AboutTranslationOptions)