from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from work.models import Work
from work.api.serializer import WorkSerializer



class WorkApyViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = WorkSerializer
    queryset = Work.objects.all()