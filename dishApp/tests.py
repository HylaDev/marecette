"""
Module: TestCase

Model: Ingredient
"""
from django.test import TestCase
from dishApp.models import Ingredient


class PostIngredient(TestCase):
    """
    Test d'ajout d'un ingrédient dans la base de données

    Method:
        testingredient: Test d'ajout de l'ingrédient "tomate" et
            une description "tomate ronde"
    """
    def test_add_ingredient(self):
        """
        Test d'ajout d'un ingrédient
        """
        post = Ingredient(name="Tomate", description="Tomate ronde")
        self.assertEqual(post.name, "Tomate")
        self.assertEqual(post.description, "Tomate ronde")
