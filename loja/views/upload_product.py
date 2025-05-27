import os
import logging
import imghdr
from decimal import Decimal
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from loja.models import Product, Categoria, ProductImage, CIDADES_CHOICES
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages

logger = logging.getLogger(__name__)

@login_required
def upload_product_view(request):
    user = request.user

    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco", "").replace(",", ".")
        descricao = request.POST.get("descricao")
        estado = request.POST.get("estado")
        categoria_id = request.POST.get("categoria")
        localidade = request.POST.get("localidade") or request.user.cidade
        images = request.FILES.getlist("images")
        tipo_venda = request.POST.get("tipo_venda")

        try:
            preco = Decimal(preco)
        except Exception:
            return render(request, "upload_product.html", {
                "categorias": Categoria.objects.all(),
                "user": user,
                "error": "O preço inserido é inválido. Use números com até duas casas decimais.",
            })

        try:
            categoria = Categoria.objects.get(id=categoria_id)
        except Categoria.DoesNotExist:
            return render(request, "upload_product.html", {
                "categorias": Categoria.objects.all(),
                "user": user,
                "error": "Categoria inválida."
            })

        # Validação estrita das imagens
        for image in images:
            if not image.content_type.startswith("image/"):
                messages.error(request, f"O ficheiro '{image.name}' não é uma imagem válida.")
                return render(request, "upload_product.html", {
                    "categorias": Categoria.objects.all(),
                    "user": user,
                    "error": f"O ficheiro {image.name} não é uma imagem válida."
                })
            if imghdr.what(image) not in ["jpeg", "png", "gif", "bmp", "tiff", "webp"]:
                messages.error(request, f"O ficheiro '{image.name}' tem uma assinatura inválida.")
                return render(request, "upload_product.html", {
                    "categorias": Categoria.objects.all(),
                    "user": user,
                    "error": f"O ficheiro {image.name} não tem uma assinatura válida de imagem."
                })

        if tipo_venda == "leilao":
            inicio_leilao = timezone.now()
            fim_leilao = inicio_leilao + timedelta(days=7)
        else:
            inicio_leilao = None
            fim_leilao = None

        product = Product.objects.create(
            nome=nome,
            preco=preco,
            descricao=descricao,
            categoria=categoria,
            localidade=localidade,
            estado=estado,
            user=user,
            tipo_venda=tipo_venda,
            inicio_leilao=inicio_leilao,
            fim_leilao=fim_leilao
        )

        product_folder = os.path.join(settings.MEDIA_ROOT, "uploads", "products", str(product.id))
        os.makedirs(product_folder, exist_ok=True)

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
    return render(request, "upload_product.html", {
        "categorias": categorias,
        "user": user,
        "CIDADES_CHOICES": CIDADES_CHOICES
    })
