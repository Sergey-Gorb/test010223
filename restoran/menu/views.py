from django.shortcuts import render
from .models import FoodCategory, Food, Topping

from django.db.models import Prefetch, Q
from django.forms import model_to_dict
from django.http import JsonResponse


def to_int(x, ret=0):  # type: (Any, int) -> int
    """
    Преобразование к целому числу, с обработкой ошибок
    """
    if x:
        try:
            x = int(x)
        except (ValueError, TypeError):
            x = ret
    else:
        x = ret
    return x


def to_bool(x):  # type: (Any) -> bool
    x = to_int(x)
    if x:
        return True
    else:
        return False


def foods(request):
    result = []
    qf = {}
    if request.POST:
        category = request.POST.get('category')
        if category:
            qf['category'] = to_int(category)
        is_special = request.POST.get('is_special')
        if is_special:
            qf['is_special'] = to_bool(is_special)
        is_vegan = request.POST.get('is_vegan')
        if is_vegan:
            qf['is_vegan']= to_bool(is_vegan)
        is_publish = request.POST.get('is_publish')
        if is_publish:
            qf['is_publish'] = to_bool(is_publish)

        toppings = request.POST.get('toppings')
        topping_set = [x for x in toppings]

        prefetch = Prefetch('toppings', queryset=Topping.objects.only('name'))
        if topping_set:
            prefetch = prefetch.filter(name__in=topping_set)
        qs = Food.objects.prefetch_related(prefetch).only('name', 'description', 'price')
        if qf:
            qs = qs.filter(**qf)
        result = []
        for food in qs:
            row = model_to_dict(food, fields=['name', 'description', 'price'])
            topings = []
            for topping in food.toppings.all():
                item = model_to_dict(topping, fields=['name'])
                topings.append(model_to_dict(item, fields=['name']))
            # you can calculate an average rating here
            row['topings'] = topings
            result.append(row)
    return JsonResponse(result)

