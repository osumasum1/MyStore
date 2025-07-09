from django.db import models

class OrderStatus(models.TextChoices):
    NEW = "NEW", "New"
    IN_PROGRESS = "IN_PROGRESS", "In Progress"
    DONE = "DONE", "Done"
    CANCELED = "CANCELED", "Canceled"
