from rest_framework.serializers import ModelSerializer
from logos.models import Logos


class LogosSerializer(ModelSerializer):
    class Meta:
        model = Logos
        fields = ['name', 'image']