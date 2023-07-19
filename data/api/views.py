from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from data.models import Data
from data.api.serializer import DataSerializer



class DataApyViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DataSerializer
    queryset = Data.objects.all()