from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from loja.models import Product, Licitacao

def produto_detail(request, id):
    produto = get_object_or_404(Product, id=id)
    return render(request, 'produto.html', {'produto': produto})

@login_required
def fazer_licitacao(request, id):
    produto = get_object_or_404(Product, id=id)
    if request.method == "POST":
        valor = float(request.POST.get('valor'))
        maior_valor = produto.maior_licitacao

        if valor > maior_valor:
            Licitacao.objects.create(produto=produto, user=request.user, valor=valor)
        else:
            return redirect('produto_detail', id=id)  # Evita lances inválidos

    return redirect('produto_detail', id=id)
