from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Product, Category
from .serializers import ProductListSerializer, CategoryListSerializer


class ListProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]


class GetProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'


class ListCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [permissions.AllowAny]


class GetCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'


class CategoryProducts(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_id = self.kwargs['id']
        return Product.objects.filter(category=category_id)
