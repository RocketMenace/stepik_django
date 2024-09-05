from django.contrib import admin
from .models import Product, ProductCategory


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category", "color", "manufacturer"]
    list_filter = ["category"]
    search_fields = ["name", "description"]
    raw_id_fields = ["category"]
    ordering = ["name"]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    list_filter = ["name"]
    search_fields = ["name", "description"]
    ordering = ["name"]
