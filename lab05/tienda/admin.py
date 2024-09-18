from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto, Cliente

# Define the custom action function
def actualizar_stock_a_20(modeladmin, request, queryset):
    # Actualiza el stock de todos los productos en el queryset a 20 unidades
    queryset.update(stock=20)

# Configura la descripción de la acción
actualizar_stock_a_20.short_description = "Actualizar stock a 20 unidades"

# Register the custom action
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    actions = [actualizar_stock_a_20]  # Añade la acción al modelo de administración de Producto
    list_display = ('categoria', 'nombre', 'precio', 'stock', 'pub_date')
    search_fields = ('categoria__nombre','nombre', 'stock')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pub_date')
    search_fields = ('nombre', 'pub_date')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nacimiento', 'pub_date')
    search_fields = ('nombres', 'dni', 'telefono')


