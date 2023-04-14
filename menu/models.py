from django.db import models


class Topping(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name
    

class CategoryFood(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name='Название'
    )
    is_publish = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(
        CategoryFood, 
        related_name='foods', 
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50, 
        verbose_name='Название'
    )
    description = models.TextField(
        blank=False, 
        verbose_name='описание',
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    is_special = models.BooleanField(
        default=False
    )
    is_vegan = models.BooleanField(
        default=False
    )
    topping = models.ManyToManyField(Topping)

    class Meta:
        verbose_name = 'еда'
        verbose_name_plural = 'еда'

    def __str__(self):
        return self.name