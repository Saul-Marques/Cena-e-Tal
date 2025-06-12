from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from loja.models import Product, Licitacao, User
from django.utils import timezone

def produto_detail(request, id):

    user = request.user
    produto = get_object_or_404(Product, id=id)
    
    # Verifica se o leilão terminou e desativa o produto se necessário
    if produto.tipo_venda == "leilao" and produto.fim_leilao and produto.fim_leilao < timezone.now() and produto.is_active:
        produto.is_active = False
        produto.save()
    

    licitacoes = produto.licitacoes.order_by('-licitado_a')  # Ordena por data descrescente (mais recente primeiro)
    vencedor = licitacoes.first().user if not produto.is_active and licitacoes.exists() else None
    
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

    if produto.tipo_venda == "leilao" and produto.fim_leilao and produto.fim_leilao < timezone.now():
        produto.is_active = False
        produto.save()
        return redirect('produto_detail', id=id)  # Redireciona sem permitir lance


    if request.method == "POST":
        valor = float(request.POST.get('valor'))
        maior_valor = produto.maior_licitacao

        if valor > maior_valor:
            Licitacao.objects.create(produto=produto, user=request.user, valor=valor)
        else:
            return redirect('produto_detail', id=id)  # Evita lances inválidos

    return redirect('produto_detail', id=id)
