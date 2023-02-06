from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"Product {self.id} - {self.name}"

