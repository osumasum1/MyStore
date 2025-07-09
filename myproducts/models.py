from django.db import models
from validators.custom_validators import validate_numbers_greater_than_zero

class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=False)
    isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[validate_numbers_greater_than_zero])
    stock = models.IntegerField(blank=False, null=False)
    category_id = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.name