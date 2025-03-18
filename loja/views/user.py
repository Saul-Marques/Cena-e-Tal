from django.shortcuts import render
from django.views import View
from loja.models import User

class UserView(View):
    def get(self, request):
        user = User.objects.filter(id=request.session["user_id"]).first()  # Obtém o utilizador autenticado
        if request.method == "POST":
            user.username = request.POST.get("nome", user.username)
            user.biografia = request.POST.get("biografia", user.biografia)
            user.localidade = request.POST.get("endereco", user.localidade)
            user.cidade = request.POST.get("cidade", user.cidade)
            user.cp = request.POST.get("cp", user.cp)
            user.telemovel = request.POST.get("telemovel", user.telemovel)
            user.email = request.POST.get("email", user.email)
            
            user.save()
            messages.success(request, "Perfil atualizado com sucesso!")

        return render(request, "users.html", {"user": user})
