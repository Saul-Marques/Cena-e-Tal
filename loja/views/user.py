from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from loja.models import User, Product, CIDADES_CHOICES
from ..utils.validators import validate_name, validate_phone_number, validate_email, validate_city
from ..utils.file_validation import validate_image_file
from ..utils.sanitizers import sanitize_user_input

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

        # Check if user is editing their own profile
        if perfil.id != request.user.id:
            messages.error(request, "Não pode editar o perfil de outro utilizador.")
            return render(request, "users.html", {
                "perfil": perfil,
                "is_owner": False,
                "cidades": CIDADES_CHOICES
            })

        # Sanitize and get form data
        post_data = sanitize_user_input(request.POST.dict())

        # Get form values
        primeiro_nome = post_data.get("primeiro_nome", perfil.primeiro_nome).strip()
        ultimo_nome = post_data.get("ultimo_nome", perfil.ultimo_nome).strip()
        biografia = post_data.get("biografia", perfil.biografia or "")
        localidade = post_data.get("endereco", perfil.localidade or "")
        cidade = post_data.get("cidade", perfil.cidade or "")
        cp = post_data.get("cp", perfil.cp or "")
        telemovel = post_data.get("telemovel", perfil.telemovel or "")
        email = post_data.get("email", perfil.email).strip().lower()

        # Validate inputs
        validation_errors = []

        # Validate names
        is_valid, error = validate_name(primeiro_nome, "Primeiro nome")
        if not is_valid:
            validation_errors.append(error)

        is_valid, error = validate_name(ultimo_nome, "Último nome")
        if not is_valid:
            validation_errors.append(error)

        # Validate phone
        if telemovel:  # Phone is optional in profile
            is_valid, error = validate_phone_number(telemovel)
            if not is_valid:
                validation_errors.append(error)

        # Validate email
        is_valid, error = validate_email(email)
        if not is_valid:
            validation_errors.append(error)
        elif email != perfil.email and User.objects.filter(email=email).exists():
            validation_errors.append("Este email já está registado!")

        # Validate city
        if cidade:
            is_valid, error = validate_city(cidade, CIDADES_CHOICES)
            if not is_valid:
                validation_errors.append(error)

        # Validate profile picture if provided
        profile_picture = request.FILES.get("profile_picture")
        if profile_picture:
            is_valid, error = validate_image_file(profile_picture, max_size_mb=2)
            if not is_valid:
                validation_errors.append(error)

        # If validation errors, return to form
        if validation_errors:
            for error in validation_errors:
                messages.error(request, error)

            produtos = Product.objects.filter(user=perfil)
            return render(request, "users.html", {
                "perfil": perfil,
                "is_owner": True,
                "produtos": produtos,
                "cidades": CIDADES_CHOICES
            })

        try:
            # Update profile fields
            perfil.primeiro_nome = primeiro_nome
            perfil.ultimo_nome = ultimo_nome
            perfil.biografia = biografia
            perfil.localidade = localidade
            perfil.cidade = cidade
            perfil.cp = cp
            perfil.telemovel = telemovel
            perfil.email = email

            # Update profile picture if provided
            if profile_picture:
                perfil.profile_picture = profile_picture

            # Save the profile
            perfil.save()
            messages.success(request, "Perfil atualizado com sucesso!")

        except Exception as e:
            messages.error(request, f"Erro ao atualizar perfil: {str(e)}")

        # Return to profile page
        produtos = Product.objects.filter(user=perfil)
        return render(request, "users.html", {
            "perfil": perfil,
            "is_owner": True,
            "produtos": produtos,
            "cidades": CIDADES_CHOICES
        })