from django.contrib import admin
from django.utils.html import format_html
from loja.models import User, Product, Categoria
from loja.models import Mensagens_de_Contactos
from loja.models import ProductImage
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "primeiro_nome", "ultimo_nome", "email", "telemovel", "profile_picture_preview", "cidade")
    search_fields = ("email", "primeiro_nome", "ultimo_nome")
    list_filter = ("email",)
    ordering = ("id",)
    readonly_fields = ["profile_picture_preview"]


    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações Pessoais", {"fields": ("primeiro_nome", "ultimo_nome", "telemovel", "profile_picture", "cidade")}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;">', obj.profile_picture.url)
        return "Sem imagem"
    
    profile_picture_preview.short_description = "Foto de Perfil"

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "categoria")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    ordering = ("id",)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)
    ordering = ("id",)

class MensagensDeContactoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "data_envio")
    search_fields = ("nome", "email")
    ordering = ("-data_envio",)

class ImagensDeProdutoAdmin(admin.ModelAdmin):
    list_display = ("product", "image")
    search_fields = ("product", )
    ordering = ("product",)

#class ProductImage(models.Model):
    #product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    #image = models.ImageField(upload_to="uploads/products/")

    #def __str__(self):
    #    return f"Image for {self.product.nome}"



# Register models
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Mensagens_de_Contactos, MensagensDeContactoAdmin)
admin.site.register(ProductImage, ImagensDeProdutoAdmin)