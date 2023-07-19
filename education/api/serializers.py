from rest_framework.serializers import ModelSerializer
from education.models import Education


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'image', 'title', 'center', 'year', 'description', 'certificate', 'created', 'updated']