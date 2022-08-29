from cgitb import html
from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from core.forms import ReservaForm


html_base ="""
<H1> MI WEB PERSONAL</H1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de...</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>    
"""

# Create your views here.
def inicio(request):
    return render(request, "core/inicio.html")


def contact(request):
    return render(request, "core/contact.html")


def reservar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
       
        if form.is_valid():
            
            form.save()
            body = f'Estimado {form.cleaned_data["nombre"]} {form.cleaned_data["apellido"]}, su reserva se ha registrado con exito \n\n\nSU PAQUETE TURISTICO CONTIENE'
            if form.cleaned_data['guia']==True:
                body += '\n\n✅  Guia Turistico'
            if form.cleaned_data['lancha']==True:
                body += '\n\n✅  Paseo en Lancha'
            if form.cleaned_data['hospedaje']==True:
                body += '\n\n✅  Hospedaje Comunitario'
            if form.cleaned_data['sendero']==True:
                body += '\n\n✅  Recorrido por Sendero Ecologico'
            if form.cleaned_data['museo']==True:
                body += '\n\n✅  Recorrido por el Museo'
            if form.cleaned_data['carpas']==True:
                body += '\n\n✅  Carpas para Sol'
                body += f'\n\nDesde {form.cleaned_data["fechaInicio"]}  Hasta {form.cleaned_data["fechaFin"]}'
            if "preciofinal" in request.POST:
                print("que si vale dice")
                body+= f'\n\n✅ Precio Final:  {request.POST.get("preciofinal")} $'
                print (request.POST.get("preciofinal"))
                
        #else: print("que no quiere guardar dice")  
            send_mail('Gracias por reservar con nosotros',
                      body,
                      'emero8060@utm.edu.ec', [form.cleaned_data['correo'], 'gabrieltheboyfaithful@gmail.com'],
                      fail_silently=False
                      )
          
        return redirect('inicio')
    else:
        form = ReservaForm()
    return render(request, "core/reservar.html", {'reservaForm': form})
