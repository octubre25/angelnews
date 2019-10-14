from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#MVT
#Model
#View
#Template
#Importaciones de Librerias Personales
from . import models
from . import forms

def listar_noticias(request):
	"""
		obtiene las noticias de la base de datos

		Retorna:
			El listado de las noticias
	"""
	#Obtiene el listado de todas las noticias
	#De la base de datos y la asigna a la variable
	#noticias
	noticias = models.Noticia.objects.all()

	#Retorna todo renderizado para ser leido en el
	#explorador, tiene tres parametros
	#Solicitud(request), palntilla de datos y datos
	return render(
					request, 
					'./noticias/index.html',
					 {'news':noticias}
				)


def ver_noticia(resquest, id_noticia):
	"""
		obtiene una noticia de la base de datos 

		parametros:
		id_noticia es numerico y hace referencia 
		al indetificador  de la noticias buscada 

		retorna 
			la noticia buscada  si existe
	"""

	noticia = models.Noticia.objects.get(id=id_noticia)

	return render (
					resquest,
						"./noticias/detalle.html",
						{"noticia":noticia}
					)



def agregar_noticias(resquest):
	"""
		Agrega una nueva noticia a la base de datos 

		Retorna
				al sitio principal de noticia
	"""

	if resquest.method == "post":
		#crea un formularionuevo con el metodo post
		form = forms.NuevaNoticiaForm(resquest.POST)

		if forms.is_valid():
			#si el formulario es valido se procede con el proceso 
			#de agregar el nuevo registro a la base de datos
			noticia = models.Noticia()
			noticia.titulo = forms.cleaned_data['titulo']
			noticia.descripcion = form.cleaned_data['descripcion']
			noticia.save()

			#Redireacciona a la pagina principal
			return HttpResponseRedirect(
							render(
									'blog:listar_noticias'
									)
							)
		else:
			return HttpResponse("Formulario invalido")
		#si el metodo de petecion no es agregar
		#se carga el formulario desde cero
		else:
			forms.NuevaNoticiaForm()

		return render (resquest, './noticias/agregar.html', {'form':form})
