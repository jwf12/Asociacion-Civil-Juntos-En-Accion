from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
	path('', views.Listar_Noticias, name = 'listar'),
	path('Detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
	path('Comentario/', views.Comentar_Noticia, name='comentar'),
	path('delete/<com_id>', views.Delete, name='borrar'),


	path('', views.Noticias_base, name='home'),
]