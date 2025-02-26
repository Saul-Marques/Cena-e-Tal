from django import forms
from loja.models import Product

from django import forms
from loja.models import Product
from decimal import Decimal

class ProductForm(forms.ModelForm):
    preco = forms.CharField(label="Preço (€)", required=True)

    class Meta:
        model = Product
        fields = ["nome", "preco", "categoria", "descricao"]

    def clean_preco(self):
        preco = self.cleaned_data["preco"].replace(",", ".")  # Converte vírgula para ponto
        try:
            preco = Decimal(preco)
        except ValueError:
            raise forms.ValidationError("Por favor, insira um valor numérico válido.")

        if preco > Decimal("99999.99"):  # Bloqueia valores acima do limite do banco
            raise forms.ValidationError("O preço não pode ser maior que 99999,99.")

        return preco
