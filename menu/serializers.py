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
            'name',
        )


class FoodSerializer(serializers.ModelSerializer):
    topping = TopingSerializer(many=True)

    class Meta:
        model = Food
        fields = ['id', 'name', 'description', 'price', 'is_vegan', 'is_special', 'topping']


class CategoryFoodSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)
    class Meta:
        model = CategoryFood
        fields = (
            'id',
            'name',
            'is_publish',
        )