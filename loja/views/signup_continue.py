# loja/views/signup_continue.py
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from loja.models import User
from django.views import View
from django.contrib import messages

class SignupContinue(View):
    def get(self, request):
        email = request.session.get("signup_email")
        cidades = User._meta.get_field("cidade").choices

        if not email:
            return redirect("signup_email"),
            
        return render(request, "signup_continue.html", {
            "email": email,
            "cidades": cidades
            })

    def post(self, request):
        email = request.session.get("signup_email")
        if not email:
            return redirect("signup_email")

        primeiro_nome = request.POST.get("primeiro_nome")
        ultimo_nome = request.POST.get("ultimo_nome")
        telemovel = request.POST.get("telemovel")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Verificar se as passwords coincidem
        if password != confirm_password:
            messages.error(request, "As passwords não coincidem.")
            return redirect("signup_continue")


        if User.objects.filter(email=email).exists():
            messages.error(request, "Este email já foi usado.")
            return redirect("signup_email")

        user = User(
            email=email,
            primeiro_nome=primeiro_nome,
            ultimo_nome=ultimo_nome,
            telemovel=telemovel,
            password=make_password(password),
        )
        user.save()
        messages.success(request, "Conta criada com sucesso! Faça login.")
        del request.session["signup_email"]
        return redirect("login")
