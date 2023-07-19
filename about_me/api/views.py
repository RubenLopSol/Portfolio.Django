from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from about_me.models import About
from about_me.api.serializers import AboutSerializer



class About_meApyViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AboutSerializer
    queryset = About.objects.all()    


