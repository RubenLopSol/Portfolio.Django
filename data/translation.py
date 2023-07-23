from modeltranslation.translator import translator, TranslationOptions
from .models import Data

# Define la traducción para el modelo Data
class DataTranslationOptions(TranslationOptions):
    fields = ('position',)  # Lista de campos que deseas traducir

# Registra la traducción para el modelo Data
translator.register(Data, DataTranslationOptions)