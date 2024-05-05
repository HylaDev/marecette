"""Importation des modules nécessaires"""
from django.test import TestCase
from django.contrib.auth.models import User
from dishApp.models import Ingredient, Dish, Season


class IngredientTestCase(TestCase):
    """Test d'ajout d'un ingrédient dans la base de données

    Method:
        test_creation_instance
    """

    def test_creation_instance(self):
        """Création et ajout d'une instance pour le test"""
        # Créez un utilisateur
        self.user = User.objects.create_user(username='testuser',  # pylint: disable:attribute-defined-outside-init
                                             email='test@gmail.com',
                                             password='testpassword')

        # Créez une instance d'ingrédient
        instance = Ingredient.objects.create(user=self.user, name='Test Name',
                                             description='Test Description')

        # Vérifiez si l'instance a été créée correctement
        self.assertEqual(instance.user, self.user)
        self.assertEqual(instance.name, 'Test Name')
        self.assertEqual(instance.description, 'Test Description')


class DishTestCase(TestCase):
    """Test d'ajout d'un plat dans la base de données

    Method:
        test_add_ingredient: Test d'ajout de l'ingrédient "tomate" et
            une description "tomate ronde"
    """

    def test_creation_instance(self):
        """Création et ajout d'une instance pour le test"""
        # Créez un utilisateur
        self.user = User.objects.create_user(username='testuser',
                                             email='test@gmail.com',
                                             password='testpassword')

        self.season = Season.objects.create(name="test",
                                            description="test description")

        # Créez une instance plat
        instance = Dish.objects.create(user=self.user, name='Test Name',
                                       season=self.season)

        # Vérifiez si l'instance a été créée
        self.assertEqual(instance.user, self.user)
        self.assertEqual(instance.name, 'Test Name')
        self.assertEqual(instance.season, self.season)
