import os
import logging
from decimal import Decimal
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from loja.models import Product, Categoria, ProductImage
from loja.forms import ProductForm

logger = logging.getLogger(__name__)

@login_required
def upload_product_view(request):
    user = request.user

    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco", "").replace(",", ".")
        descricao = request.POST.get("descricao")
        categoria_id = request.POST.get("categoria")
        images = request.FILES.getlist("images")

        try:
            preco = Decimal(preco)
        except Exception:
            return render(request, "upload_product.html", {
                "categorias": Categoria.objects.all(),
                "user": user,
                "error": "O preço inserido é inválido. Use números com até duas casas decimais."
            })

        try:
            categoria = Categoria.objects.get(id=categoria_id)
        except Categoria.DoesNotExist:
            return render(request, "upload_product.html", {
                "categorias": Categoria.objects.all(),
                "user": user,
                "error": "Categoria inválida."
            })

        product = Product.objects.create(
            nome=nome,
            preco=preco,
            descricao=descricao,
            categoria=categoria,
            user=user 
        )

        product_folder = os.path.join(settings.MEDIA_ROOT, "uploads", "products", str(product.id))
        os.makedirs(product_folder, exist_ok=True)

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

                ProductImage.objects.create(product=product, image=relative_image_path)

            except Exception as e:
                logger.error(f"❌ Erro ao guardar imagem {image_name}: {e}")

        return redirect("homepage")

    categorias = Categoria.objects.all()
    return render(request, "upload_product.html", {"categorias": categorias, "user": user})
