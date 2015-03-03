from django.db import models
from django import forms

class services(models.Model):
	"""docstring for services"""
	title = models.CharField(max_length=80)
	Description = models.TextField()
	imagePath = models.CharField(max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control','data-toggle':'tooltip',
    	'data-placement':'top','title':'Nombre obligatorio!'}))
    message = forms.CharField(required=True,widget=forms.Textarea(attrs={'class' : 'form-control', 'data-toggle':'tooltip',
    	'data-placement':'top','title':'Mensaje obligatorio!'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control', 'data-toggle':'tooltip',
    	'data-placement':'top','title':'Mail obligatorio!'}))
    cc_myself = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class':'checkbox'}))

"""class FormularioContacto(forms.Form):
	correo = forms.EmailField(label='correo', max_length=200)#(widget=forms.TextInput(attrs={'class' : 'form-control'}))
	nombre = forms.CharField(label='nombre', max_length=80) #, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	mensaje = forms.CharField(label='mensaje')#(widget=forms.Textarea(attrs={'class' : 'form-control'}))"""



			
						
		
