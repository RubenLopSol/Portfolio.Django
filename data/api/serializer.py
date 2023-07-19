from rest_framework.serializers import ModelSerializer
from data.models import Data


class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ['image', 'name', 'position', 'gitHub', 'linkedin', 'cv', 'updated', 'created']