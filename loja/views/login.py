from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from loja.models import User
from django.views import View
from django.contrib import messages

class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.get_user_by_email(email)  

        if user and check_password(password, user.password):
            request.session["user_id"] = user.id 
            return redirect("homepage")
        else:
            messages.error(request, "Email ou senha inválidos. Tente novamente.")
            return render(request, "login.html")
