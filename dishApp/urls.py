"""Importation des modules nécessaires"""
from django.urls import path
from .views import dashboard, sign_up, sign_in, add_dish
from .views import add_ingredient, add_ingredient_to_dish
from .views import select_saison, recommend_dish_by_season, select_dish
from .views import generate_shopping_list, search, dish_list, user_logout

urlpatterns = [
     path('', dashboard, name='dashboard'),
     path('inscription', sign_up, name='inscription'),
     path('connexion', sign_in, name='connexion'),
     path('deconnexion', user_logout, name='deconnexion'),
     path('ajout_plat', add_dish, name='ajout_plat'),
     path('ajout_ingredient', add_ingredient, name='ajout_ingredient'),
     path('ajout_ingredient_à_plat', add_ingredient_to_dish,
          name='ajout_ingredient_à_plat'),
     path('choix_saison', select_saison,
          name='choix_saison'),
     path('choix_plat', select_dish, name='choix_plat'),
     path('liste_de_course/<int:id>', generate_shopping_list,
          name='liste_de_course'),
     path('recherche/', search, name="recherche"),
     path('conseiller_plat/<int:id>', recommend_dish_by_season,
          name='conseiller_plat'),
     path('plats/', dish_list,
          name='plats'),
]
