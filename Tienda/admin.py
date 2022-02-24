from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=("creado", "actualizado")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("creado", "actualizado")

admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)


