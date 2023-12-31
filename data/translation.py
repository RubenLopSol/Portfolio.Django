from modeltranslation.translator import translator, TranslationOptions
from .models import Data

# Define la traducción para el modelo Data
class DataTranslationOptions(TranslationOptions):
    fields = ('position_en', 'position_es')  # Lista de campos que deseas traducir

# Registra la traducción para el modelo Data
translator.register(Data, DataTranslationOptions)