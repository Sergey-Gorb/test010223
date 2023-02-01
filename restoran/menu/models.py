from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=255)
    is_publish = models.BooleanField()

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField()
    is_special = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=True)
    toppings = models.ManyToManyField(Topping, related_name='foods')

    def __str__(self):
        return self.name

