from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from loja.models import User, Product, CIDADES_CHOICES
import re
from django.core.validators import ValidationError

@method_decorator(login_required, name='dispatch')
class UserView(View):
    def get(self, request, user_id):
        perfil = get_object_or_404(User, id=user_id)
        produtos = Product.objects.filter(user=perfil)
        return render(request, "users.html", {
            "perfil": perfil,
            "is_owner": perfil.id == request.user.id,
            "produtos": produtos,
            "cidades": CIDADES_CHOICES
        })

    def post(self, request, user_id):
        perfil = get_object_or_404(User, id=user_id)
        if perfil.id != request.user.id:
            messages.error(request, "Não pode editar o perfil de outro utilizador.")
            return render(request, "users.html", {
                "perfil": perfil,
                "is_owner": False,
                "cidades": CIDADES_CHOICES
            })

        # Atualiza os campos
        perfil.primeiro_nome = request.POST.get("primeiro_nome", perfil.primeiro_nome)
        if request.FILES.get("profile_picture"):
            perfil.profile_picture = request.FILES["profile_picture"]
        perfil.ultimo_nome = request.POST.get("ultimo_nome", perfil.ultimo_nome)
        perfil.biografia = request.POST.get("biografia", perfil.biografia)
        perfil.localidade = request.POST.get("endereco", perfil.localidade)
        perfil.cidade = request.POST.get("cidade", perfil.cidade)
        perfil.cp = request.POST.get("cp", perfil.cp)
        perfil.telemovel = request.POST.get("telemovel", perfil.telemovel)
        if perfil.telemovel and not re.fullmatch(r"9\d{8}", perfil.telemovel):
            messages.error(request, "Número de telemóvel inválido. Deve começar por 9 e ter 9 dígitos.")
            return render(request, "users.html", {
            "perfil": perfil,
            "is_owner": True,
            "cidades": CIDADES_CHOICES
        })

        perfil.email = request.POST.get("email", perfil.email)

        perfil.save()
        messages.success(request, "Perfil atualizado com sucesso!")

        produtos = Product.objects.filter(user=perfil)
        return render(request, "users.html", {
            "perfil": perfil,
            "is_owner": True,
            "produtos": produtos,
            "cidades": CIDADES_CHOICES
        })