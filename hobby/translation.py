from modeltranslation.translator import translator, TranslationOptions
from .models import Hobby

# Define la traducción para el modelo Hobby
class HobbyTranslationOptions(TranslationOptions):
    fields = ('title_en', 'title_es', 'description_en', 'description_es',)  # Lista de campos que deseas traducir

# Registra la traducción para el modelo Hobby
translator.register(Hobby, HobbyTranslationOptions)