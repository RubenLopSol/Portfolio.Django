from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from hobby.models import Hobby
from hobby.api.serializers import HobbySerializer



class HobbyApyViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = HobbySerializer
    queryset = Hobby.objects.all()    


