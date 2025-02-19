from django import forms
from loja.models import Product

class ProductForm(forms.ModelForm):
    preco = forms.CharField(label="Preço (€)")

    class Meta:
        model = Product
        fields = ["nome", "preco", "categoria", "descricao"]

    def clean_preco(self):
        preco = self.cleaned_data["preco"].replace(",", ".")
        try:
            return round(float(preco), 2)
        except ValueError:
            raise forms.ValidationError("Insira um valor válido para o preço.")