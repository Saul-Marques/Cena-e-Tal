from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from loja.models import User
from django.views import View
from django.contrib import messages

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        primeiro_nome = postData.get('primeironome')
        ultimo_nome = postData.get('ultimonome')
        telemovel = postData.get('telemovel')
        email = postData.get('email')
        password = postData.get('password')

        # Preserve form values in case of an error
        value = {
            'primeiro_nome': primeiro_nome,
            'ultimo_nome': ultimo_nome,
            'telemovel': telemovel,
            'email': email
        }

        # Instantiate user correctly
        user = User(
            primeiro_nome=primeiro_nome,
            ultimo_nome=ultimo_nome,
            telemovel=telemovel,
            email=email,
            password=password
        )

        # Validate user input
        error_message = self.validateUser(user)

        if not error_message:
            user.password = make_password(user.password)  # Hash password
            user.save()  # Save user to database
            messages.success(request, "Registro concluído com sucesso! Faça login.")
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateUser(self, user):
        error_message = None
        if not user.primeiro_nome:
            error_message = "Por favor, insira o seu primeiro nome!"
        elif len(user.primeiro_nome) < 3:
            error_message = "O primeiro nome deve ter pelo menos 3 caracteres."
        elif not user.ultimo_nome:
            error_message = "Por favor, insira o seu último nome!"
        elif len(user.ultimo_nome) < 3:
            error_message = "O último nome deve ter pelo menos 3 caracteres."
        elif not user.telemovel:
            error_message = "Por favor, insira o seu número de telemóvel!"
        elif len(user.telemovel) < 9:
            error_message = "O número de telemóvel deve ter 9 caracteres."
        elif len(user.password) < 5:
            error_message = "A senha deve ter pelo menos 5 caracteres."
        elif len(user.email) < 5:
            error_message = "O email deve ter pelo menos 5 caracteres."
        elif User.objects.filter(email=user.email).exists():
            error_message = "Este email já está registado!"

        return error_message
