import email
from django.shortcuts import redirect, render
from .form import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == "POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("Nombre")
            email=request.POST.get("Email")
            mensaje=request.POST.get("Mensaje")

            email = EmailMessage("Mensaje desde App DJango", "El usuario con nombre {} con la dirección {} escribe lo siguiente: \n\n {}".format(nombre,email,mensaje), 
            "", ["vallrack67@gmai.com"], reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

            return redirect("/contacto/?valido")
    return render(request,"Contacto/contacto.html", {"miFormulario": formulario_contacto})