from django.contrib import admin

from menu.models import (
    Topping, 
    CategoryFood, 
    Food
    )


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoryFood)
class CategoryFoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Food)
class  FoodAdmin(admin.ModelAdmin):
    pass
