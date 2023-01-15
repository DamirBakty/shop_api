from rest_framework import serializers

from api import models

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
