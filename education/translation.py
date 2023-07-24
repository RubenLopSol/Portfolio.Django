from modeltranslation.translator import translator, TranslationOptions
from .models import Education

# Define la traducción para el modelo Education
class EducationTranslationOptions(TranslationOptions):
    fields = ('title_en', 'title_es', 'description_en', 'description_es', )  # Lista de campos que deseas traducir

# Registra la traducción para el modelo Education
translator.register(Education, EducationTranslationOptions)