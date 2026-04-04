import os
import logging
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from loja.models import Product, Categoria, ProductImage, CIDADES_CHOICES
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from ..utils.validators import validate_price, validate_city
from ..utils.file_validation import validate_multiple_images, get_safe_filename
from ..utils.sanitizers import sanitize_product_description, sanitize_user_input

logger = logging.getLogger(__name__)

@login_required
def upload_product_view(request):
    user = request.user

    if request.method == "POST":
        # Sanitize and get form data
        post_data = sanitize_user_input(request.POST.dict())

        nome = post_data.get("nome", "").strip()
        preco_str = post_data.get("preco", "")
        descricao = sanitize_product_description(post_data.get("descricao", ""))
        estado = post_data.get("estado")
        categoria_id = post_data.get("categoria")
        localidade = post_data.get("localidade") or user.cidade
        images = request.FILES.getlist("images")
        tipo_venda = post_data.get("tipo_venda")

        # Validate required fields
        validation_errors = []

        if not nome:
            validation_errors.append("Nome do produto é obrigatório")
        elif len(nome) < 3:
            validation_errors.append("Nome do produto deve ter pelo menos 3 caracteres")

        # Validate price
        preco, price_error = validate_price(preco_str)
        if price_error:
            validation_errors.append(price_error)

        # Validate category
        try:
            categoria = Categoria.objects.get(id=categoria_id)
        except (Categoria.DoesNotExist, ValueError, TypeError):
            validation_errors.append("Categoria inválida")

        # Validate city
        if localidade:
            is_valid, city_error = validate_city(localidade, CIDADES_CHOICES)
            if not is_valid:
                validation_errors.append(city_error)

        # Validate sale type
        if tipo_venda not in ['venda', 'leilao']:
            validation_errors.append("Tipo de venda inválido")

        # Validate images
        is_valid, image_error, valid_images = validate_multiple_images(images, max_size_mb=5, max_count=10)
        if not is_valid:
            validation_errors.append(image_error)

        # If validation errors, return to form
        if validation_errors:
            for error in validation_errors:
                messages.error(request, error)

            categorias = Categoria.objects.all()
            return render(request, "upload_product.html", {
                "categorias": categorias,
                "user": user,
                "CIDADES_CHOICES": CIDADES_CHOICES,
                "form_data": {
                    "nome": nome,
                    "preco": preco_str,
                    "descricao": descricao,
                    "estado": estado,
                    "categoria_id": categoria_id,
                    "localidade": localidade,
                    "tipo_venda": tipo_venda
                }
            })

        # Set auction times if applicable
        if tipo_venda == "leilao":
            inicio_leilao = timezone.now()
            fim_leilao = inicio_leilao + timedelta(days=7)

            # Validate auction end time is in the future
            if fim_leilao <= timezone.now():
                messages.error(request, "O fim do leilão deve ser no futuro")
                return redirect("upload_product")
        else:
            inicio_leilao = None
            fim_leilao = None

        try:
            # Use atomic transaction to ensure data consistency
            with transaction.atomic():
                # Create product
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

                # Create product folder
                product_folder = os.path.join(settings.MEDIA_ROOT, "uploads", "products", str(product.id))
                os.makedirs(product_folder, exist_ok=True)

                # Save images
                for image in valid_images:
                    try:
                        # Get safe filename
                        safe_filename = get_safe_filename(image)
                        image_path = os.path.join(product_folder, safe_filename)
                        relative_image_path = f"uploads/products/{product.id}/{safe_filename}"

                        # Save file
                        with open(image_path, "wb+") as destination:
                            for chunk in image.chunks():
                                destination.write(chunk)

                        # Create ProductImage record
                        ProductImage.objects.create(product=product, image=relative_image_path)

                    except Exception as e:
                        logger.error(f"❌ Erro ao guardar imagem {safe_filename}: {e}")
                        # Continue with other images even if one fails

            messages.success(request, "Produto criado com sucesso!")
            return redirect("homepage")

        except Exception as e:
            logger.error(f"❌ Erro ao criar produto: {e}")
            messages.error(request, "Ocorreu um erro ao criar o produto. Tente novamente.")

            categorias = Categoria.objects.all()
            return render(request, "upload_product.html", {
                "categorias": categorias,
                "user": user,
                "CIDADES_CHOICES": CIDADES_CHOICES,
                "form_data": {
                    "nome": nome,
                    "preco": preco_str,
                    "descricao": descricao,
                    "estado": estado,
                    "categoria_id": categoria_id,
                    "localidade": localidade,
                    "tipo_venda": tipo_venda
                }
            })

    # GET request - show form
    categorias = Categoria.objects.all()
    return render(request, "upload_product.html", {
        "categorias": categorias,
        "user": user,
        "CIDADES_CHOICES": CIDADES_CHOICES
    })
