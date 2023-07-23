from modeltranslation.translator import translator, TranslationOptions
from .models import Work

# Define la traducción para el modelo Work
class WorkTranslationOptions(TranslationOptions):
    fields = ( 'company', 'description', )  # Lista de campos que deseas traducir

# Registra la traducción para el modelo Work
translator.register(Work, WorkTranslationOptions)