from django.shortcuts import render, redirect
from loja.models import User, Product, Categoria
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        produtos = Product.objects.all()
        
        
        user = None
        if 'user_id' in request.session:  
            user = User.objects.filter(id=request.session['user_id']).first()  

        return render(request, "index.html", {"categorias": categorias, "produtos": produtos, "user": user})


        
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