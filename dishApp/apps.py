"""Importation des modules nécessaires
"""
from django.apps import AppConfig


class DishappConfig(AppConfig):
    """Créer la configuration de l'application locale
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dishApp'
