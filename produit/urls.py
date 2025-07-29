from django.urls import path
from . import views

urlpatterns = [
    path('produits/', views.getProduits, name='get_produits'),
    path('produits/<int:id>/', views.getProduitById, name='get_produit_by_id'),
    path('produits/add/', views.addProduit, name='add_produit'),
    path('produits/update/<int:id>/', views.updateProduit, name='update_produit'),
    path('produits/delete/<int:id>/', views.deleteProduit, name='delete_produit'),
]
