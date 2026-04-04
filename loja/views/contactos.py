from django.shortcuts import render, redirect
from django.contrib import messages
from loja.models import Mensagens_de_Contactos
from ..utils.validators import validate_name, validate_email
from ..utils.sanitizers import sanitize_user_input, sanitize_text

def contactos_view(request):
    if request.method == "POST":
        # Sanitize input
        post_data = sanitize_user_input(request.POST.dict())

        nome = post_data.get("nome", "").strip()
        email = post_data.get("email", "").strip().lower()
        mensagem = sanitize_text(post_data.get("mensagem", ""))

        # Validate inputs
        validation_errors = []

        # Validate name
        is_valid, error = validate_name(nome, "Nome")
        if not is_valid:
            validation_errors.append(error)

        # Validate email
        is_valid, error = validate_email(email)
        if not is_valid:
            validation_errors.append(error)

        # Validate message
        if not mensagem.strip():
            validation_errors.append("Mensagem é obrigatória")
        elif len(mensagem.strip()) < 10:
            validation_errors.append("Mensagem deve ter pelo menos 10 caracteres")
        elif len(mensagem) > 1000:
            validation_errors.append("Mensagem não pode exceder 1000 caracteres")

        # If validation errors, return to form
        if validation_errors:
            for error in validation_errors:
                messages.error(request, error)

            return render(request, "contactos.html", {
                "form_data": {
                    "nome": nome,
                    "email": email,
                    "mensagem": mensagem
                }
            })

        try:
            # Create contact message
            Mensagens_de_Contactos.objects.create(
                nome=nome,
                email=email,
                mensagem=mensagem
            )

            messages.success(request, "A sua mensagem foi enviada com sucesso!")
            return redirect("homepage")

        except Exception as e:
            messages.error(request, "Ocorreu um erro ao enviar a mensagem. Tente novamente.")
            # Log the error for debugging
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Contact form error: {str(e)}")

            return render(request, "contactos.html", {
                "form_data": {
                    "nome": nome,
                    "email": email,
                    "mensagem": mensagem
                }
            })

    return render(request, "contactos.html")