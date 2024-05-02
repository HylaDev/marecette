"""Importation des modules nécessaires
"""
from django.contrib import admin
from django.urls import path, include
admin.site.site_header = 'MaRecette'
admin.site.index_title = "Espace admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dishApp.urls')),
]
