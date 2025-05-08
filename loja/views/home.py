import random
import os
from django.conf import settings
from django.shortcuts import render, redirect
from loja.models import User, Product, Categoria
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        categoria_id = request.GET.get('categoria')
                
        if categoria_id:
            produtos = Product.objects.filter(categoria__id=categoria_id)
        else:
            produtos = Product.objects.all()
        
        user = request.user

        covers_folder = os.path.join(settings.BASE_DIR, 'loja', 'static', 'imgs', 'covers')
        all_images = [f for f in os.listdir(covers_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        selected_image = random.choice(all_images) if all_images else 'cover2.png'  # fallback se vazio
        selected_image_url = f'imgs/covers/{selected_image}'


        return render(request, "index.html", {
            "categorias": categorias,
            "produtos": produtos,
            "user": user,
            "cover_image": selected_image_url})

        
def loja(request):
    products = None
    categorias = Categoria.get_all_categorias()
    categoriaID = request.GET.get('categoria')
    if categoriaID:
        products = Products.get_all_products_by_categoriaid(categoriaID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categorias'] = categorias

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)