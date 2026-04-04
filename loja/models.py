from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError
from .utils.validators import validate_phone_number, validate_email, validate_name


class UserManager(BaseUserManager):
    def create_user(self, email, primeiro_nome, ultimo_nome, telemovel, password=None):
        """
        Create and save a regular user with hashed password.
        """
        # Validate inputs
        if not email:
            raise ValueError("O email é obrigatório!")

        is_valid, error = validate_email(email)
        if not is_valid:
            raise ValueError(f"Email inválido: {error}")

        is_valid, error = validate_name(primeiro_nome, "Primeiro nome")
        if not is_valid:
            raise ValueError(f"Primeiro nome inválido: {error}")

        is_valid, error = validate_name(ultimo_nome, "Último nome")
        if not is_valid:
            raise ValueError(f"Último nome inválido: {error}")

        is_valid, error = validate_phone_number(telemovel)
        if not is_valid:
            raise ValueError(f"Telemóvel inválido: {error}")

        # Create user with normalized email
        user = self.model(
            email=self.normalize_email(email),
            primeiro_nome=primeiro_nome.strip(),
            ultimo_nome=ultimo_nome.strip(),
            telemovel=telemovel
        )

        # Set and hash password immediately
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

class User(AbstractBaseUser, PermissionsMixin):
    # Name fields with validation
    primeiro_nome = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2, message="Primeiro nome deve ter pelo menos 2 caracteres"),
            RegexValidator(
                regex=r'^[a-zA-ZÀ-ÿ\s\'-]+$',
                message="Primeiro nome só pode conter letras, espaços, hífens e apóstrofos"
            )
        ]
    )
    ultimo_nome = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2, message="Último nome deve ter pelo menos 2 caracteres"),
            RegexValidator(
                regex=r'^[a-zA-ZÀ-ÿ\s\'-]+$',
                message="Último nome só pode conter letras, espaços, hífens e apóstrofos"
            )
        ]
    )

    # Phone with regex validation
    telemovel = models.CharField(
        max_length=9,  # Changed from 10 to match validation
        validators=[
            RegexValidator(
                regex=r'^9\d{8}$',
                message="Telemóvel deve começar com 9 e ter exatamente 9 dígitos"
            )
        ],
        blank=True,
        null=True
    )

    email = models.EmailField(unique=True)

    # Profile fields
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    localidade = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(
        max_length=255,
        choices=CIDADES_CHOICES,
        blank=True,
        null=True
    )
    cp = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\d{4}-\d{3}$',
                message="Código postal deve estar no formato 0000-000"
            )
        ]
    )
    biografia = models.TextField(blank=True, null=True)

    objects = UserManager()

    # Django admin required fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["primeiro_nome", "ultimo_nome", "telemovel"]

    def clean(self):
        """Additional model-level validation"""
        from .utils.validators import validate_phone_number, validate_email

        # Validate email format
        is_valid, error = validate_email(self.email)
        if not is_valid:
            raise ValidationError({"email": error})

        # Validate phone if provided
        if self.telemovel:
            is_valid, error = validate_phone_number(self.telemovel)
            if not is_valid:
                raise ValidationError({"telemovel": error})

    def save(self, *args, **kwargs):
        """Ensure clean is called before save"""
        self.clean()
        super().save(*args, **kwargs)

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
        ('1', 'Mau'),
        ('2', 'Muito Usado'),
        ('3', 'Usado'),
        ('4', 'Ligeiramente Usado'),
        ('5', 'Como novo'),
    ]
    TIPO_VENDA_CHOICES = [
        ('venda', 'Venda Direta'),
        ('leilao', 'Leilão'),
    ]

    tipo_venda = models.CharField(
        max_length=10,
        choices=TIPO_VENDA_CHOICES,
        default='venda'
    )
    data_adicionado = models.DateTimeField(auto_now_add=True)
    inicio_leilao = models.DateTimeField(null=True, blank=True)
    fim_leilao = models.DateTimeField(null=True, blank=True)
    localidade = models.CharField(
        max_length=255,
        choices=CIDADES_CHOICES,
        blank=True,
        null=True
    )

    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='3'
    )
    nome = models.CharField(
        max_length=60,
        validators=[
            MinLengthValidator(3, message="Nome do produto deve ter pelo menos 3 caracteres")
        ]
    )
    preco = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01, message="Preço deve ser positivo")
        ]
    )
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, default=1)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


    @property
    def maior_licitacao(self):
        maior = self.licitacoes.aggregate(models.Max('valor'))['valor__max']
        return maior if maior else 0  # Se não houver licitações, retorna o preço base

    def __str__(self):
        return f"{self.nome} - {self.get_estado_display()}"


class Licitacao(models.Model):
    produto = models.ForeignKey(Product, related_name='licitacoes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01, message="Valor da licitação deve ser positivo")
        ]
    )
    licitado_a = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent duplicate bids from same user on same product
        unique_together = ['produto', 'user']

    def clean(self):
        """Validate bid amount"""
        from .utils.validators import validate_bid_amount

        if self.produto and self.valor:
            current_max = self.produto.maior_licitacao
            is_valid, error = validate_bid_amount(self.valor, current_max)
            if not is_valid:
                raise ValidationError({"valor": error})

            # Check that user isn't bidding on their own product
            if self.user == self.produto.user:
                raise ValidationError("Não pode licitar no seu próprio produto")

    def save(self, *args, **kwargs):
        """Ensure clean is called before save"""
        self.clean()
        super().save(*args, **kwargs)


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