from django.db import models
from validators.custom_validators import validate_only_contains_chars_and_space
    
class Clients(models.Model):
    name = models.CharField(max_length=255,validators=[validate_only_contains_chars_and_space])
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def __str__(self):
        return self.name