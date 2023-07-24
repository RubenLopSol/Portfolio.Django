from rest_framework.serializers import ModelSerializer
from work.models import Work


class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = ['company', 'position', 'year', 'description_en', 'description_es', 'logo']