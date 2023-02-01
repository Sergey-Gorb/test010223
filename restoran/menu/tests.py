from django.test import TestCase
from django.urls import reverse

from .models import Food, FoodCategory, Topping


class FoodCategoryTests(TestCase):

    def setUp(self):
        FoodCategory.objects.create(
            name='Drinks',
            is_publish=True
        )

        Food.objects.create(
            name='Cafe',
            category=1,
            description = 'Very best',
            price = 120,
            is_special = True,
            is_vegan = False,
            is_publish = False,
        )

        Food.objects.create(
            name='Tee',
            category=1,
            description='China tee',
            price=220,
            is_special=True,
            is_vegan=True,
            is_publish=True
        )

        Topping.objects.create(name='Acuker', foods=1)
        Topping.objects.create(name='Cream', foods=2)

    def test_category_content(self):
        category = FoodCategory.objects.get(id=1)
        expected_object_name = f'{category.name}'
        self.assertEquals(expected_object_name, 'Drinks')

    def test_food_content(self):
        food = Food.objects.get(id=1)
        expected_object_name = f'{food.name}'
        self.assertEquals(expected_object_name, 'Cafe')

    def test_Topping_content(self):
        topping = Topping.objects.get(id=1)
        expected_object_name = f'{topping.name}'
        self.assertEquals(expected_object_name, 'Acuker')

