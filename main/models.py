import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('boots', 'Boots'),
        ('ball', 'Ball'),
        ('accessories', 'Accessories'),
        ('merch', 'Merch'),
    ]

    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)

    # tetap: created_at
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return self.name
    

