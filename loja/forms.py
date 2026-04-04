from django import forms
from loja.models import Product, User
from ..utils.validators import validate_price
from ..utils.sanitizers import sanitize_product_description


class ProductForm(forms.ModelForm):
    preco = forms.CharField(
        label="Preço (€)",
        required=True,
        help_text="Use ponto ou vírgula como separador decimal"
    )

    class Meta:
        model = Product
        fields = ["nome", "preco", "categoria", "descricao", "estado", "localidade", "tipo_venda"]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_preco(self):
        preco_str = self.cleaned_data["preco"]
        preco, error = validate_price(preco_str)

        if error:
            raise forms.ValidationError(error)

        return preco

    def clean_descricao(self):
        descricao = self.cleaned_data.get("descricao", "")
        return sanitize_product_description(descricao)

    def clean_nome(self):
        nome = self.cleaned_data.get("nome", "").strip()
        if len(nome) < 3:
            raise forms.ValidationError("Nome do produto deve ter pelo menos 3 caracteres")
        return nome


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "primeiro_nome", "ultimo_nome", "email", "telemovel",
            "biografia", "localidade", "cidade", "cp", "profile_picture"
        ]
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 4}),
            'profile_picture': forms.FileInput(attrs={'accept': 'image/*'}),
        }

    def clean_telemovel(self):
        telemovel = self.cleaned_data.get("telemovel", "").strip()
        if telemovel and not telemovel.startswith('9') or len(telemovel) != 9:
            raise forms.ValidationError("Telemóvel deve começar com 9 e ter 9 dígitos")
        return telemovel

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip().lower()
        if not email or '@' not in email or '.' not in email.split('@')[-1]:
            raise forms.ValidationError("Email inválido")
        return email

    def clean_cp(self):
        cp = self.cleaned_data.get("cp", "").strip()
        if cp and not (cp.replace('-', '').isdigit() and len(cp.replace('-', '')) == 7):
            raise forms.ValidationError("Código postal deve estar no formato 0000-000")
        return cp
