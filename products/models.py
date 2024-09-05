from django.db import models

# Create your models here.

NULLABLE = {"null": True,
            "blank": True, }


class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Product(models.Model):
    class Color(models.TextChoices):
        BLACK = "Black"
        WHITE = "White"
        BLUE = "Blue"
        BROWN = "Brown"

    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products_images", **NULLABLE)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    color = models.CharField(max_length=10, choices=Color.choices, default=Color.BLUE)
    manufacturer = models.CharField(max_length=200, **NULLABLE)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return f"{self.name}"
