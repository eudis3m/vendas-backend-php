from django.shortcuts import render # type: ignore
from rest_framework import viewsets # type: ignore
from .models import Product, Sale
from .serializers import ProductSerializer, SaleSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
