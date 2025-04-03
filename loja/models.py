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


    def create_superuser(self, email, primeiro_nome, ultimo_nome, telemovel, password=None):
        user = self.create_user(
            email=email,
            primeiro_nome=primeiro_nome,
            ultimo_nome=ultimo_nome,
            telemovel=telemovel,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_user_by_email(self, email):
        return self.filter(email=email).first()

def user_directory_path(instance, filename):
    return f'uploads/profiles/{instance.id}/{filename}'

# Lista de opções para a cidade
CIDADES_CHOICES = [
    ('aveiro', 'Aveiro'),
    ('beja', 'Beja'),
    ('braga', 'Braga'),
    ('braganca', 'Bragança'),
    ('castelo_branco', 'Castelo Branco'),
    ('coimbra', 'Coimbra'),
    ('evora', 'Évora'),
    ('faro', 'Faro'),
    ('guarda', 'Guarda'),
    ('leiria', 'Leiria'),
    ('lisboa', 'Lisboa'),
    ('portalegre', 'Portalegre'),
    ('porto', 'Porto'),
    ('santarem', 'Santarém'),
    ('setubal', 'Setúbal'),
    ('viana_do_castelo', 'Viana do Castelo'),
    ('vila_real', 'Vila Real'),
    ('viseu', 'Viseu'),
]

class User(AbstractBaseUser):
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    telemovel = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)    
    localidade = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(
        max_length=255,
        choices=CIDADES_CHOICES,
        blank=True,
        null=True
    )
    cp = models.CharField(max_length=20, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    
    objects = UserManager()
    # Novos campos necessários para o Django Admin
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["primeiro_nome", "ultimo_nome", "telemovel"]
    def has_perm(self, perm, obj=None):
        return True  # Modify as needed

    def has_module_perms(self, app_label):
        return True

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    icon = models.FileField(default=None, blank=True, null=True, upload_to='uploads/categorias/')

    @staticmethod
    def get_all_categorias(): 
        return Categoria.objects.all()

    def __str__(self):
        return self.nome


def product_image_upload_path(instance, filename):
    return f"uploads/products/{instance.product.id}/{filename}"

class Product(models.Model):
    ESTADO_CHOICES = [
        ('novo', 'Como novo'),
        ('bom', 'Bom'),
        ('mau', 'Mau'),
    ]

    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='bom'  # Define "Bom" como o padrão, pode alterar conforme necessário
    )
    nome = models.CharField(max_length=60)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, default=1)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    @property
    def maior_licitacao(self):
        maior = self.licitacoes.aggregate(models.Max('valor'))['valor__max']
        return maior if maior else 0  # Se não houver licitações, retorna o preço base

    def __str__(self):
        return f"{self.nome} - {self.get_estado_display()}"


class Licitacao(models.Model):
    produto = models.ForeignKey(Product, related_name='licitacoes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    licitado_a = models.DateTimeField(auto_now_add=True)


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