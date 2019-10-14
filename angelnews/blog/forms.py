from django import forms


from .models import *


class NuevaNoticiaForm(forms.Form):
	titulo = forms.CharField(label="Titulo")
	descripcion = forms.CharField(label="Descripcion")