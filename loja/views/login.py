import random
import os
from django.conf import settings
from django.shortcuts import render, redirect
from loja.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from ..utils.validators import validate_email
from ..utils.sanitizers import sanitize_user_input


class Login(View):
    def get(self, request):
        covers_folder = os.path.join(settings.BASE_DIR, 'loja', 'static', 'imgs', 'covers_login')
        all_images = [f for f in os.listdir(covers_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        selected_image = random.choice(all_images) if all_images else 'drphil.png'
        selected_image_url = f'imgs/covers_login/{selected_image}'

        return render(request, "login.html", {"cover_image": selected_image_url})

    def post(self, request):
        # Sanitize input
        post_data = sanitize_user_input(request.POST.dict())

        email = post_data.get("username", "").strip().lower()
        password = post_data.get("password", "")

        # Basic validation
        validation_errors = []

        # Validate email format
        is_valid, error = validate_email(email)
        if not is_valid:
            validation_errors.append(error)

        # Validate password
        if not password:
            validation_errors.append("Password é obrigatória")
        elif len(password) < 1:  # Minimum 1 character for password validation
            validation_errors.append("Password inválida")

        # If validation errors, return to form
        if validation_errors:
            for error in validation_errors:
                messages.error(request, error)
            return render(request, "login.html")

        # Authenticate using Django's system
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect("homepage")
            else:
                messages.error(request, "A sua conta está desativada.")
        else:
            # Don't reveal whether email exists or password is wrong
            messages.error(request, "Email ou senha inválidos. Tente novamente.")

        return render(request, "login.html")
