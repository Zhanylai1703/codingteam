from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from menu.serializers import (
    FoodSerializer,
)
from menu.models import (
    CategoryFood,
    Food
)


class FoodListView(generics.ListAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        is_vegan = self.request.GET.get('is_vegan', None)
        is_special = self.request.GET.get('is_special', None)
        toping_names = self.request.GET.getlist('toping_name', [])

        if is_vegan is not None:
            queryset = queryset.filter(is_vegan=is_vegan)

        if is_special is not None:
            queryset = queryset.filter(is_special=is_special)

        if toping_names:
            queryset = queryset.filter(toping__name__in=toping_names)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        categories = CategoryFood.objects.filter(foods__in=queryset).distinct()
        result = []
        for category in categories:
            category_data = {
                'id': category.id,
                'name': category.name,
                'foods': self.get_serializer(queryset.filter(category=category), many=True).data
            }
            result.append(category_data)

        return Response(result)
