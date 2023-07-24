from modeltranslation.translator import translator, TranslationOptions
from .models import Work

# Define la traducción para el modelo Work
class WorkTranslationOptions(TranslationOptions):
    fields = ( 'description_en', 'description_es' )  # Lista de campos que deseas traducir

# Registra la traducción para el modelo Work
translator.register(Work, WorkTranslationOptions)