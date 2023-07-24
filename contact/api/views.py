from rest_framework import viewsets
from contact.models import Contact
from contact.api.serializers import ContactSerializer

from ..forms import FormularioContacto
from django.core.mail import EmailMessage
import traceback
from dotenv import load_dotenv
import os

load_dotenv()


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


    @staticmethod
    def send_contact_email(name, email, message):
        email_message = EmailMessage("Mensaje desde App Django", 
                                    "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(name, email, message),
                                    "", [os.environ.get("EMAIL_HOST_USER")], reply_to=[email])
        try:
            email_message.send()
        except Exception as e:
            traceback.print_exc()

    def create(self, request, *args, **kwargs):
        # Handle the contact form submission here
        formulario_contacto = FormularioContacto(data=request.data)
        if formulario_contacto.is_valid():
            name = formulario_contacto.cleaned_data["name"]
            email = formulario_contacto.cleaned_data["email"]
            message = formulario_contacto.cleaned_data["message"]
            self.send_contact_email(name, email, message)
        return super().create(request, *args, **kwargs)