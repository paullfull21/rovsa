from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import ContactForm
from django.core.mail import EmailMessage
from django.core.mail import send_mail


def home(request):
	return render(request,'index.html')

def clientes(request):
	return render(request,'clientes.html')

def aboutUs(request):
	return render(request,'aboutUs.html')

def contacto(request):
	if request.method == 'POST':#SI EL FORMULARIO FU ENVIADO
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']
			recipients = ['paulfulll20@gmail.com']
			if cc_myself:
				recipients.append(sender)

			send_mail(subject, message, sender, recipients)
	else:
		form = ContactForm()

	return render(request, 'contactUs.html', {'form': form})

def gracias(request):
	html='<html><body><h1>"gracias por emviarnos tus comentarios"</h1></body></html>'
	return HttpResponse(html)

def servicioUno(request):
	return render(request,'servicioUno.html')

def servicioDos(request):
	return render(request,'servicioDos.html')

def servicioTres(request):
	return render(request, 'servicioTres.html')




	
