from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from produit.models import Produit
from .serializers import ProduitSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@api_view(['GET'])
def getProduits(request):
    name = request.query_params.get('name')
    if name:
        produits = Produit.objects.filter(name__icontains=name)
    else:
        produits = Produit.objects.all()
    serializer = ProduitSerializer(produits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduitById(request, id):
    try:
        produit = Produit.objects.get(pk=id)
    except Produit.DoesNotExist:
        return Response({"error": "Produit not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProduitSerializer(produit)
    return Response(serializer.data)


@api_view(['GET'])
def getProduitByName(request):
    name = request.query_params.get('name')
    if not name:
        return Response({"error": "Name parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

    produits = Produit.objects.filter(name__icontains=name)
    serializer = ProduitSerializer(produits, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    request_body=ProduitSerializer 
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def addProduit(request):
    name = request.data.get('name')
    if Produit.objects.filter(name__iexact=name).exists():
        return Response({"error": "Produit with this name already exists."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ProduitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='put',
    request_body=ProduitSerializer
)
@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
def updateProduit(request, id):
    try:
        produit = Produit.objects.get(pk=id)
    except Produit.DoesNotExist:
        return Response({"error": "Produit not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProduitSerializer(produit, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteProduit(request, id):
    try:
        produit = Produit.objects.get(pk=id)
    except Produit.DoesNotExist:
        return Response({"error": "Produit not found."}, status=status.HTTP_404_NOT_FOUND)

    produit.delete()
    return Response({"message": "Produit deleted."}, status=status.HTTP_204_NO_CONTENT)
