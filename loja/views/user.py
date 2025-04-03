from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class UserView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        return render(request, "users.html", {"user": user})
    
    @method_decorator(login_required)
    def post(self, request):
        user = request.user
        user.primeiro_nome = request.POST.get("primeiro_nome", user.primeiro_nome)
        if request.FILES.get("profile_picture"):
            user.profile_picture = request.FILES["profile_picture"]        
        user.ultimo_nome = request.POST.get("ultimo_nome", user.primeiro_nome)
        user.biografia = request.POST.get("biografia", user.biografia)
        user.localidade = request.POST.get("endereco", user.localidade)
        user.cidade = request.POST.get("cidade", user.cidade)
        user.cp = request.POST.get("cp", user.cp)
        user.telemovel = request.POST.get("telemovel", user.telemovel)
        user.email = request.POST.get("email", user.email)

        user.save()
        messages.success(request, "Perfil atualizado com sucesso!")

        return render(request, "users.html", {"user": user})
