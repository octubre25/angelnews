from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#MVT
#Model
#View
#Template
#Importaciones de Librerias Personales
from . import models


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