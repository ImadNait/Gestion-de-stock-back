from rest_framework import serializers
from produit.models import Produit

class ProduitSerializer (serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'