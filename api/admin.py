from django.contrib import admin
from .models import User, ShoppingList, Product

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name')  # Отображение полей в списке
    search_fields = ('user_id','user_name')  # Поля для поиска

@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('list_id', 'list_name')
    search_fields = ('list_id', 'list_name')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'unit', 'count', 'bought')
    search_fields = ('product_id', 'product_name')
