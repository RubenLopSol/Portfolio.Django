from rest_framework.serializers import ModelSerializer
from hobby.models import Hobby


class HobbySerializer(ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['id', 'title', 'description', 'image', 'created', 'updated']