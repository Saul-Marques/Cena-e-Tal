import os
from django.conf import settings
from django.shortcuts import render, redirect
from loja.models import Product, Categoria, ProductImage
from decimal import Decimal

def upload_product_view(request):
    if "user_id" not in request.session:
        return redirect("login")

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

        # Criar a pasta para o produto dentro de MEDIA_ROOT/uploads/products/{id}
        product_folder = os.path.join(settings.MEDIA_ROOT, "uploads", "products", str(product.id))
        os.makedirs(product_folder, exist_ok=True)

        # Salvar as imagens dentro da pasta do produto
        for image in images:
            image_name = image.name.replace(" ", "_")  # Evita espaços nos nomes dos arquivos
            image_path = f"uploads/products/{product.id}/{image_name}"
            full_image_path = os.path.join(settings.MEDIA_ROOT, image_path)

            with open(full_image_path, "wb+") as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            # Salvar o caminho RELATIVO no banco de dados
            ProductImage.objects.create(product=product, image=image_path)

        return redirect("homepage")

    categorias = Categoria.objects.all()
    return render(request, "upload_product.html", {"categorias": categorias})
