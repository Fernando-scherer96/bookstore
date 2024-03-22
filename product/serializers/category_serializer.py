from rest_framework import serializers

from product.Models.category import Category

class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category
        fields = [
            'title', 
            'slug', 
            'description', 
            'active',
        ]