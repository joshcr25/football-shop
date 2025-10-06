import uuid
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey (Baju seragam)'),
        ('bola', 'Bola'),
]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tambahkan ini
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255)
    price = models.IntegerField(default = 200000)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    thumbnail = models.URLField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    brand = models.CharField(max_length=255)
    year_of_manufacture = models.IntegerField(default=2025) # Tahun pembuatan produk
    year_of_product = models.IntegerField(default=2025) # Tahun produk muncul di toko bola
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    