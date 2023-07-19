from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from logos.models import Logos
from logos.api.serializers import LogosSerializer



class LogosApyViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = LogosSerializer
    queryset = Logos.objects.all()