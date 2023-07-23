from modeltranslation.translator import translator, TranslationOptions
from .models import Education

# Define la traducción para el modelo Education
class EducationTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )  # Lista de campos que deseas traducir

# Registra la traducción para el modelo Education
translator.register(Education, EducationTranslationOptions)