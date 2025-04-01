from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from loja.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
            email = request.POST["username"]
            password = request.POST["password"]

            # Authenticate using Django's system
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)  # ✅ This sets up session & request.user
                return redirect("homepage")
            else:
                messages.error(request, "Email ou senha inválidos. Tente novamente.")
                return render(request, "login.html")
