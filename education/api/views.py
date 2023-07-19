from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from education.models import Education
from education.api.serializers import EducationSerializer



class EducationApyViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EducationSerializer
    queryset = Education.objects.all()   