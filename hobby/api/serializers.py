from rest_framework.serializers import ModelSerializer
from hobby.models import Hobby


class HobbySerializer(ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['id', 'title_en', 'title_es', 'description_en', 'description_es', 'image', 'created', 'updated']