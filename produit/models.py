from django.db import models

class Produit(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='products/', blank=True)
    quantite = models.PositiveIntegerField(default=0)
