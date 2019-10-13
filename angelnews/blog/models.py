from django.db import models

class Noticia(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=1000)
	fecha_pub = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s %s" % (self.titulo,self.fecha_pub)