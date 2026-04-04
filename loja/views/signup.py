from django.shortcuts import render, redirect
from loja.models import User
from django.views import View
from django.contrib import messages
from ..utils.validators import (
    validate_name, validate_phone_number, validate_email, validate_password
)
from ..utils.sanitizers import sanitize_user_input


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        # Get and sanitize form data
        post_data = sanitize_user_input(request.POST.dict())

        primeiro_nome = post_data.get('primeironome', '').strip()
        ultimo_nome = post_data.get('ultimonome', '').strip()
        telemovel = post_data.get('telemovel', '').strip()
        email = post_data.get('email', '').strip().lower()
        password = post_data.get('password', '')

        # Preserve form values in case of an error
        value = {
            'primeiro_nome': primeiro_nome,
            'ultimo_nome': ultimo_nome,
            'telemovel': telemovel,
            'email': email
        }

        # Validate all inputs
        validation_errors = []

        # Validate first name
        is_valid, error = validate_name(primeiro_nome, "Primeiro nome")
        if not is_valid:
            validation_errors.append(error)

        # Validate last name
        is_valid, error = validate_name(ultimo_nome, "Último nome")
        if not is_valid:
            validation_errors.append(error)

        # Validate phone
        is_valid, error = validate_phone_number(telemovel)
        if not is_valid:
            validation_errors.append(error)

        # Validate email
        is_valid, error = validate_email(email)
        if not is_valid:
            validation_errors.append(error)
        elif User.objects.filter(email=email).exists():
            validation_errors.append("Este email já está registado!")

        # Validate password
        is_valid, error = validate_password(password)
        if not is_valid:
            validation_errors.append(error)

        # If validation errors, return to form
        if validation_errors:
            messages.error(request, " ".join(validation_errors))
            return render(request, 'signup.html', {'values': value})

        try:
            # Create user using UserManager (password is hashed automatically)
            user = User.objects.create_user(
                email=email,
                primeiro_nome=primeiro_nome,
                ultimo_nome=ultimo_nome,
                telemovel=telemovel,
                password=password
            )

            messages.success(request, "Registro concluído com sucesso! Faça login.")
            return redirect('homepage')

        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'signup.html', {'values': value})
        except Exception as e:
            messages.error(request, "Ocorreu um erro durante o registo. Tente novamente.")
            # Log the actual error for debugging
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Signup error: {str(e)}")
            return render(request, 'signup.html', {'values': value})
