"""Importation des modules nécessaires
"""
from django.contrib import admin
from .models import Season, Dish, Ingredient, IngredientList

admin.site.register(Season)
admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(IngredientList)
