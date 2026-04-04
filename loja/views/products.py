from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils import timezone
from django.contrib import messages
from loja.models import Product, Licitacao, User
from ..utils.validators import validate_bid_amount
from ..utils.sanitizers import sanitize_user_input

def produto_detail(request, id):
    user = request.user
    produto = get_object_or_404(Product, id=id)

    # Check if auction has ended and deactivate product if necessary
    if (produto.tipo_venda == "leilao" and
        produto.fim_leilao and
        produto.fim_leilao < timezone.now() and
        produto.is_active):

        produto.is_active = False
        produto.save()

    # Get bids ordered by date (most recent first)
    licitacoes = produto.licitacoes.order_by('-licitado_a')

    # Determine winner if auction has ended
    vencedor = None
    if not produto.is_active and licitacoes.exists():
        vencedor = licitacoes.first().user

    return render(request, 'produto.html', {
        'produto': produto,
        'licitacoes': licitacoes,
        'user': user,
        'tipo_venda': produto.tipo_venda,
        'vencedor': vencedor,
    })

@login_required
def fazer_licitacao(request, id):
    produto = get_object_or_404(Product, id=id)

    # Check if auction has ended
    if produto.tipo_venda == "leilao" and produto.fim_leilao and produto.fim_leilao < timezone.now():
        produto.is_active = False
        produto.save()
        messages.error(request, "Este leilão já terminou.")
        return redirect('produto_detail', id=id)

    # Check if product is active
    if not produto.is_active:
        messages.error(request, "Este produto não está disponível para licitações.")
        return redirect('produto_detail', id=id)

    # Check if user is trying to bid on their own product
    if produto.user == request.user:
        messages.error(request, "Não pode licitar no seu próprio produto.")
        return redirect('produto_detail', id=id)

    if request.method == "POST":
        # Sanitize input
        post_data = sanitize_user_input(request.POST.dict())
        valor_str = post_data.get('valor', '0')

        try:
            valor = float(valor_str)
        except ValueError:
            messages.error(request, "Valor da licitação inválido.")
            return redirect('produto_detail', id=id)

        # Get current maximum bid
        maior_valor = produto.maior_licitacao

        # Validate bid amount
        is_valid, error = validate_bid_amount(valor, maior_valor, min_increment=0.01)
        if not is_valid:
            messages.error(request, error)
            return redirect('produto_detail', id=id)

        try:
            # Use atomic transaction to ensure data consistency
            with transaction.atomic():
                # Create bid
                Licitacao.objects.create(
                    produto=produto,
                    user=request.user,
                    valor=valor
                )

                messages.success(request, "Licitação realizada com sucesso!")

        except Exception as e:
            messages.error(request, f"Erro ao realizar licitação: {str(e)}")

    return redirect('produto_detail', id=id)
