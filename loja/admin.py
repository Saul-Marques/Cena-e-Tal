from django.contrib import admin
from loja.models import User, Product, Categoria
from loja.models import Mensagens_de_Contactos
from loja.models import ProductImage
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "primeiro_nome", "ultimo_nome", "email", "telemovel")
    search_fields = ("email", "primeiro_nome", "ultimo_nome")
    list_filter = ("email",)
    ordering = ("id",)

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