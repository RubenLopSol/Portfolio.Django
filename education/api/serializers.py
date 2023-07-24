from rest_framework.serializers import ModelSerializer
from education.models import Education


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'image', 'title_en', 'title_es', 'center', 'year', 'description_en', 'description_es', 'certificate', 'created', 'updated']