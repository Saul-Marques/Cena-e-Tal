from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, primeiro_nome, ultimo_nome, telemovel, password=None):
        if not email:
            raise ValueError("O email é obrigatório!")
        user = self.model(
            email=self.normalize_email(email),
            primeiro_nome=primeiro_nome,
            ultimo_nome=ultimo_nome,
            telemovel=telemovel
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_user_by_email(self, email):
        return self.filter(email=email).first()

class User(AbstractBaseUser):
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    telemovel = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["primeiro_nome", "ultimo_nome", "telemovel"]

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    icon = models.FileField(default=None, blank=True, null=True, upload_to='uploads/categorias/')

    @staticmethod
    def get_all_categorias(): 
        return Categoria.objects.all()

    def __str__(self):
        return self.nome


def product_image_upload_path(instance, filename):
    """Retorna o caminho correto para armazenar imagens de produtos."""
    return f"uploads/products/{instance.product.id}/{filename}"

class Product(models.Model):
    nome = models.CharField(max_length=60)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, default=1)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)  # ✅ Ligação com o usuário

    def __str__(self):
        return self.nome


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/products/")

    def __str__(self):
        return f"Image for {self.product.nome}"

class Mensagens_de_Contactos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome} ({self.email})"