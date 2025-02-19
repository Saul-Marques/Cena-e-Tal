from django.shortcuts import render, redirect
from django.contrib import messages
from loja.models import Mensagens_de_Contactos

def contactos_view(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        mensagem = request.POST["mensagem"]

        
        Mensagens_de_Contactos.objects.create(nome=nome, email=email, mensagem=mensagem)

        messages.success(request, "A sua mensagem foi enviada com sucesso!")
        return redirect("homepage")  

    return render(request, "contactos.html")