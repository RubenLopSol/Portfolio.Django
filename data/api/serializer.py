from rest_framework.serializers import ModelSerializer
from data.models import Data


class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ['image', 'name', 'position_en', 'position_es', 'gitHub', 'linkedin', 'cv', 'updated', 'created']