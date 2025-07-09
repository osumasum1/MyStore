from django.db import models
from myclients.models import Clients 
from myproducts.models import Products 
from .enums.order_status import OrderStatus

class Orders(models.Model):
    order_number = models.CharField(max_length=20)
    client_id = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.NEW)

    class Meta:
        verbose_name = ("Pedido")
        verbose_name_plural = ("Pedidos")

    def __str__(self):
        return f"Pedido {self.order_number}: {self.client_id.name} - {self.product_id.name}"