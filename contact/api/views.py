from rest_framework import viewsets
from contact.models import Contact
from contact.api.serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer