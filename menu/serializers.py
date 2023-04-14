from rest_framework import serializers

from menu.models import (
    Topping,
    CategoryFood,
    Food
)


class TopingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = (
            'name'
        )


class CategoryFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryFood
        fields = (
            'name',
            'is_publish',
        )


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = (
            'category',
            'name',
            'description',
            'price',
            'is_special',
            'is_vegan',
            'topping',
        )