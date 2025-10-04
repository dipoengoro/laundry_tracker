from rest_framework import serializers
from .models import ClothingItem

class ClothingItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ClothingItem
        fields = ['id', 'owner', 'name', 'category', 'color', 'image', 'created_at', 'updated_at']