# loja/views/signup_email.py
from django.shortcuts import render, redirect
from loja.models import User
from django.views import View
from django.contrib import messages

class SignupEmailCheck(View):
    def get(self, request):
        return render(request, "signup_email.html")

    def post(self, request):
        email = request.POST.get("email")

        if not email or len(email) < 5:
            messages.error(request, "Insira um email válido.")
            return render(request, "signup_email.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Este email já está registado.")
            return render(request, "signup_email.html")

        request.session["signup_email"] = email
        return redirect("signup_continue")
