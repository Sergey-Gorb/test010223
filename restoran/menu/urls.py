from django.urls import path, include
from .views import foods

urlpatterns = [
   path(r'foods^$', foods)
]