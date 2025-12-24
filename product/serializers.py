from rest_framework import serializers
from .models import Product, Category, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
from django.contrib import admin
# from .models import Product, Category, Review   

# admin.site.register(Product)    
# admin.site.register(Category)       
# admin.site.register(Review)
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category']

class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Review
        fields = ['id', 'product', 'text'] 

        