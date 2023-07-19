from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.conf import settings
import traceback
from dotenv import load_dotenv
import os

load_dotenv()


def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            name = formulario_contacto.cleaned_data["name"]
            email = formulario_contacto.cleaned_data["email"]
            message = formulario_contacto.cleaned_data["message"]
            
            email = EmailMessage("Mensaje desde App Django", 
                                 "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(name, email, message),
                                 "", [os.environ.get("EMAIL_HOST_USER")], reply_to=[email])
            try:
                email.send()
                return redirect("/contact/?valido")
            except Exception as e:
                error_message = "An error occurred while sending the email."
                traceback.print_exc()
                return redirect("/contact/?novalido"), error_message

    return render(request, "contacto/contact.html", {'miFormulario': formulario_contacto})