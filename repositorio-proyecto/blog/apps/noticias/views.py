from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Noticia, Categoria
# Create your views here.

@login_required
def Listar_Noticias(request):
	contexto = {}

	id_categoria = request.GET.get('id', None)

	if id_categoria:
		n = Noticia.objects.filter(categoria_noticia = id_categoria)
	else:
		n = Noticia.objects.all()

	contexto['noticia'] = n

	cat = Categoria.objects.all().order_by('categoria')
	contexto['categorias'] = cat
	return render(request, 'noticias/listar.html', contexto)



@login_required
def Detalle_Noticias(request, pk):
	contexto = {}
	n = Noticia.objects.get(pk = pk)
	contexto['noticia'] = n
	return render(request, 'noticias/detalle.html', contexto)



def Noticias_base(request):
	contexto ={}

	nDate = Noticia.objects.all().order_by('fecha')[:3] # Esto es para mostrar los...
	#ultimos tres por fecha. (va a servir para el aside)
	contexto['notiFecha'] = nDate

	return render(request, 't_home.html', contexto) 