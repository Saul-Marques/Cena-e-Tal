from django.shortcuts import render
from django.views import View
from loja.models import Categoria

class CategoriaView(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, "categorias.html", {"categorias": categorias})
