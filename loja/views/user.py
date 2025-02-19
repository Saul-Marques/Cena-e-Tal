from django.shortcuts import render
from django.views import View
from loja.models import User

class UserView(View):
    def get(self, request):
        usuarios = User.objects.all()
        return render(request, "users.html", {"usuarios": usuarios})
