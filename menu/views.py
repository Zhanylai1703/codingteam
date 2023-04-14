from django.shortcuts import render

from rest_framework import generics

from menu.serializers import (
    TopingSerializer,
    CategoryFoodSerializer,
    FoodSerializer,
)
from menu.models import (
    Topping,
    CategoryFood,
    Food
)


class FoodListAPIView(generics.ListAPIView):
    serializer_class = CategoryFoodSerializer

    def get_queryset(self):
        qs = CategoryFood.objects.filter(foods__is_published=True).distinct()
        is_vegan = self.request.query_params.get('is_vegan')
        is_special = self.request.query_params.get('is_special')
        topping = self.request.query_params.get('topping')

        if is_vegan:
            qs = qs.filter(foods__is_vegan=is_vegan)

        if is_special:
            qs = qs.filter(foods__is_special=is_special)

        if topping:
            qs = qs.filter(foods__toppings__name__icontains=topping)

        return qs