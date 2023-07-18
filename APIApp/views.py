
from rest_framework import generics
from APIApp.models import Product
from APIApp.serializers import ProductSerializer


class AllProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SpecificProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
