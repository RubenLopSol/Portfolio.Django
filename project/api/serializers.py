from rest_framework.serializers import ModelSerializer
from project.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'image', 'description', 'deployment', 'code_front', 'code_back', 'created']