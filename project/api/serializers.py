from rest_framework.serializers import ModelSerializer
from project.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title_en', 'title_es', 'image', 'description_en', 'description_es', 'deployment', 'code_front', 'code_back', 'created']