from django.shortcuts import render
from django.views import View
from loja.models import Product

class ProductView(View):
    def get(self, request):
        produtos = Product.objects.all()
        return render(request, "products.html", {"produtos": produtos})
