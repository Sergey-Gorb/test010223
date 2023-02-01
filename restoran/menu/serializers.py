from rest_framework import serializers
from .models import Food, FoodCategory, Topping


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price', ]