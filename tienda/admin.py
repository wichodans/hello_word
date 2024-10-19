from django.contrib import admin
from .models import Categoria_Prod, Producto

# Register your models here.
class Categoria_Prod_Admin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class Producto_Admin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register (Categoria_Prod, Categoria_Prod_Admin)
admin.site.register (Producto, Producto_Admin)