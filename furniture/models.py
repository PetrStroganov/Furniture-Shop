from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse


class FurnitureType(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name


class Furniture(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField(validators=[MaxValueValidator(100000, "Стоимость мебели не должна превышать 100тыс руб"), MinValueValidator(500, "Стоимость мебели не может быть ниже 500 руб") ])
    type = models.ForeignKey(FurnitureType, on_delete=models.CASCADE, related_name="furniture_type")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="furnitures")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("furniture-detail", args=[self.slug])    