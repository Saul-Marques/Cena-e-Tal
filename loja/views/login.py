import random
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from loja.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login


class Login(View):
    def get(self, request):

        covers_folder = os.path.join(settings.BASE_DIR, 'loja', 'static', 'imgs', 'covers_login')
        all_images = [f for f in os.listdir(covers_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        selected_image = random.choice(all_images) if all_images else 'drphil.png'
        selected_image_url = f'imgs/covers_login/{selected_image}'
            
        return render(request, "login.html", {"cover_image": selected_image_url})

    def post(self, request):
            email = request.POST["username"]
            password = request.POST["password"]

            # Authenticate using Django's system
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                messages.error(request, "Email ou senha inválidos. Tente novamente.")


            return render(request, "login.html")
