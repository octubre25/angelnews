from django.urls import path


from . import views

app_name = "blog"

urlpatterns = [
	path('', views.listar_noticias, name="listar_noticias"),
	path("<int:id_noticia>/", views.ver_noticia,  name="ver_noticia")
]
