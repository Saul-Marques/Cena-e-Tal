import os
import logging
from django.conf import settings
from django.shortcuts import render, redirect
from loja.models import Product, Categoria, ProductImage, User
from decimal import Decimal
from loja.forms import ProductForm

def upload_product_view(request):
    
    if "user_id" not in request.session:
        return redirect("login")

    user = User.objects.filter(id=request.session["user_id"]).first()  # Obtém o utilizador autenticado

    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco").replace(",", ".")
        descricao = request.POST.get("descricao")
        categoria_id = request.POST.get("categoria")
        images = request.FILES.getlist("images")

        try:
            preco = Decimal(preco)
        except ValueError:
            return render(request, "upload_product.html", {
                "categorias": Categoria.objects.all(),
                "user": user,  # Passa o utilizador para o template
                "error": "O preço inserido é inválido. Use números com até duas casas decimais."
            })

        categoria = Categoria.objects.get(id=categoria_id)
        product = Product(
            nome=nome,
            preco=preco,
            descricao=descricao,
            categoria=categoria,
            user_id=request.session["user_id"]
        )
        product.save()

        # Criar a pasta do produto se não existir
        product_folder = os.path.join(settings.MEDIA_ROOT, "uploads", "products", str(product.id))
        os.makedirs(product_folder, exist_ok=True)

        # Verificar se imagens foram enviadas
        if not images:
            logger.warning(f"⚠ Nenhuma imagem foi enviada para o produto {product.id}")

        for image in images:
            image_name = image.name.replace(" ", "_")
            image_path = os.path.join(product_folder, image_name)
            relative_image_path = f"uploads/products/{product.id}/{image_name}"

            try:
                with open(image_path, "wb+") as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)

                product_image = ProductImage.objects.create(product=product, image=relative_image_path)

            except Exception as e:
                logger.error(f" Erro ao guardar imagem {image_name}: {e}")

        return redirect("homepage")

    categorias = Categoria.objects.all()
    return render(request, "upload_product.html", {"categorias": categorias, "user": user})
