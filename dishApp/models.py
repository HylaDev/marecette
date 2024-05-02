"""Importation des modules nécessaires
"""
from django.db import models
from django.contrib.auth.models import User


class Season(models.Model):
    """
    Table "Season" dans la base de données

    Attributes:
        name (CharField): Le nom de la saison
        description (TextField): Description de la saison

    Methods:
        __str__: Retourne le nom de la saison sur l'espace admin
    """
    name = models.CharField(verbose_name="Nom de la saison", max_length=100)
    description = models.TextField(verbose_name="Description", blank=False)

    def __str__(self):
        return str(self.name)


class Dish(models.Model):
    """
    Table "Dish" dans la base de données

    Attributes:
        user (ForeignKey): Clé étrangère de l'utilisateur qui a créé ce plat
        name (CharField): Le nom du plat
        season (ForeignKey): Clé étrangère de la saison associée à ce plat

    Methods:
        __str__: Retourne le nom du plat sur l'espace admin

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    name = models.CharField(verbose_name="Nom du plat", max_length=100)
    season = models.ForeignKey(Season,
                               on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return str(self.name)


class Ingredient(models.Model):
    """
    Table "Ingredient" dans la base de données

    Attributes:
        name (CharField): Nom de l'ingredient
        description (TextField): Description de l'ingrédient

    Methods:
        __str__: Retourne le nom de l'ingredient sur l'espace admin
    """
    user = user = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name="+")
    name = models.CharField(verbose_name="Nom de l'ingrédient", max_length=100)
    description = models.TextField(verbose_name="Description", blank=False)

    def __str__(self):
        return str(self.name)


class IngredientList(models.Model):
    """
    Table "IngredientList" dans la base de données

    Attributes:
        dish (ForeignKey): Clé étrangère du plat associé à cette liste
            d'ingredient
        ingredient (ForeignKey): Clé étrangère de l'ingredient contenu
            à cette liste d'ingredient
        quantity (CharField): Quantité d'un ingrédient dans la liste
            d'ingrédient

    Methods:
        __str__: Retourne le nom du plat associé à cette liste d'ingrédient
    """
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE,
                             related_name="+")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   related_name="+")
    quantity = models.CharField(max_length=25, null=False)

    def __str__(self):
        return str(self.dish.name)
