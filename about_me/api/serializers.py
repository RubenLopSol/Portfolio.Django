from rest_framework.serializers import ModelSerializer
from about_me.models import About



class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'description', 'image', 'created', 'updated']
