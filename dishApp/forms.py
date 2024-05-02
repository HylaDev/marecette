"""Importation des modules nécessaires
"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Dish, Ingredient, IngredientList


class SignUpForm(UserCreationForm):  # pylint: disable=too-many-ancestors
    """Formulaire d'inscription
    """
    class Meta:  # pylint: disable=too-few-public-methods
        """Metadata de la table 'User'

        Attributes:
            model (Model):  La table à utiliser
            fields (list): Liste des champs du formulaire
        """
        model = User
        fields = ('username', 'email', 'password1')


class AddDishForm(forms.ModelForm):
    """Formulaire d'ajout de plat
    """
    class Meta:  # pylint: disable=too-few-public-methods
        """Metadata de la table 'Dish'

        Attributes:
            model (Model):  La table à utiliser
            fields (list): Liste des champs du formulaire
        """
        model = Dish
        fields = ['user', 'name', 'season']


class AddIngredientForm(forms.ModelForm):
    """Formulaire d'ajout d'ingrédient
    """
    class Meta:  # pylint: disable=too-few-public-methods
        """Metadata de la table 'Ingredient'

        Attributes:
            model (Model):  La table à utiliser
            fields (list): Liste des champs du formulaire
        """
        model = Ingredient
        fields = ['user', 'name', 'description']


class AddIngredientToDishForm(forms.ModelForm):
    """Formulaire d'ajout d'un ingrédient à un plat
    """
    class Meta:  # pylint: disable=too-few-public-methods
        """Metadata de la table 'IngredientList'

        Attributes:
            model (Model):  La table à utiliser
            fields (list): Liste des champs du formulaire
        """
        model = IngredientList
        fields = ['dish', 'ingredient', 'quantity']
