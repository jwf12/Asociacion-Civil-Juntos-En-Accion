from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Noticia
# Create your views here.

@login_required
def Listar_Noticias(request):
	contexto = {}

	n = Noticia.objects.all()
	contexto['noticia'] = n

	return render(request, 'noticias/listar.html', contexto)



@login_required
def Detalle_Noticias(request, pk):
	contexto = {}
	return render(request, 'noticias/detalle.html', contexto)



def Noticias_base (request):
	ctxtDate ={}

	nDate = Noticia.objects.all().order_by('fecha')[:3] # Esto es para mostrar los...
	#ultimos tres por fecha. (va a servir para el aside)
	ctxtDate['notiFecha'] = nDate

	return render(request, 'usuarios/t_home.html', ctxtDate) 