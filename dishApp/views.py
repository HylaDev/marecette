"""Importation des modules nécessaires"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import SignUpForm, AddDishForm, AddIngredientForm
from .forms import AddIngredientToDishForm
from .models import Season, Dish, Ingredient, IngredientList


@login_required(login_url='connexion')
def dashboard(request):
    """Tableau de board

    Affiche la page "dashboard" qui présente le nombre de plats et d'ingrédient
    ajoutés par l'utilisateur connecté

    Args:
        request: Requête entrante

    Context:
        user (User): L'utilisateur connecté
        dishs (int): Le nombre de plat ajouté
        ingredients (int): Le nombre d'ingrédient ajouté
    """
    user = request.user
    dishs = Dish.objects.filter(user=user).count()  # pylint: disable=maybe-no-member
    ingredients = Ingredient.objects.filter(user=user).count()  # pylint: disable=maybe-no-member
    context = {'user': user,
               'dishs': dishs,
               'ingredients': ingredients
               }
    return render(request, 'profils/dashboard.html', context)


@login_required(login_url='connexion')
def dish_list(request):
    """Affiche la liste des plats

    Args:
        request: Requête entrante

    Context:
        dishs (list): Liste des plats ajoutés dans la
            base de données
    """
    user = request.user
    dishs = Dish.objects.filter(user=user)  # pylint: disable=maybe-no-member
    context = {
        'dishs': dishs
    }
    return render(request, 'profils/dishs.html', context)


def sign_up(request):
    """Création de compte utilisateur

    Args:
        request: Requête entrante

    Context:
        form (str): Le formulaire d'inscription
    """
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Compte bien crée')
                return redirect('dashboard')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'profils/inscription.html', context)


def sign_in(request):
    """Connexion d'un utilisateur

    Pour la connexion, l'utilisateur doit renseigné son username et son
    password

    Args:
        request: Requête entrante
    """
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Vous êtes bien connecté')
            return redirect('dashboard')
    return render(request, 'profils/connexion.html')


@login_required(login_url='connexion')
def add_dish(request):
    """Ajout d'un plat

    Args:
        request: Requête entrante

    Context:
        seasons (list): La liste des saisons ajoutées
        user (User): L'utilisateur connecté
    """
    user = request.user
    seasons = Season.objects.all()  # pylint: disable=maybe-no-member
    if request.method == 'POST':
        form = AddDishForm(request.POST)
        if form.is_valid():
            print('je suis ici')
            form.save()
            messages.success(request, 'Plat bien ajouté')
            return redirect('dashboard')
    else:
        form = AddDishForm(request.POST)

    context = {'seasons': seasons, 'user': user}
    return render(request, 'profils/add_dish.html', context)


@login_required(login_url='connexion')
def add_ingredient(request):
    """Ajout d'un ingrédient

    Args:
        request: Requête entrante

    Context:
        user (User): L'utilisateur connecté
    """
    user = request.user
    if request.method == 'POST':
        form = AddIngredientForm(request.POST)
        if form.is_valid():
            form.save()  # pylint: disable=maybe-no-member
            messages.success(request, 'Ingredient bien ajouté')
            return redirect('ajout_ingredient')
    else:
        form = AddIngredientForm(request.POST)

    context = {'user': user}
    return render(request, 'profils/add_ingredient.html', context)


@login_required(login_url='connexion')
def add_ingredient_to_dish(request):
    """Ajouter un ingrédient à un plat

    Args:
        request: Requête entrante

    Context:
        user (User): L'utilisateur connecté
        ingredients (list): Liste des ingrédients ajoutés dans la
            base de données
        dishs (list): Liste des plats ajoutés dans la
            base de données
    """
    ingredients = Ingredient.objects.all()  # pylint: disable=maybe-no-member
    dishs = Dish.objects.all()  # pylint: disable=maybe-no-member
    user = request.user
    if request.method == 'POST':
        form = AddIngredientToDishForm(request.POST)
        if form.is_valid():
            form.save()
            ingredient = form.cleaned_data['ingredient']
            plat = form.cleaned_data['dish']
            messages.success(request,
                             f'{ingredient} bien ajouté au plat {plat}')
            return redirect('dashboard')
    else:
        form = AddIngredientToDishForm(request.POST)

    context = {
        'user': user,
        'ingredients': ingredients,
        'dishs': dishs
        }
    return render(request, 'profils/add_ingredient_to_dish.html', context)


@login_required(login_url='connexion')
def select_saison(request):
    """Choix de saison

    Args:
        request: Requête entrante

    Context:
        saisons (list): Liste des saisons ajoutées dans la
            base de données
    """
    seasons = Season.objects.all()  # pylint: disable=maybe-no-member
    context = {
        'seasons': seasons
    }
    return render(request, 'profils/select_season.html', context)


@login_required(login_url='connexion')
def recommend_dish_by_season(request, id):  # pylint: disable=redefined-builtin
    """Recommander un plat par saison

    Args:
        request: Requête entrante

    Context:
        saison (int): id de la saison associée au plat
        dishs (list): Liste des plats liés à la saison sélectionné
    """
    dishs = Dish.objects.filter(    # pylint: disable=maybe-no-member
        season=id, user=request.user)
    for dish in dishs:
        season = dish.season
    context = {
        'dishs': dishs,
        'season': season
    }
    return render(request, 'profils/recommend_dishes.html', context)


@login_required(login_url='connexion')
def select_dish(request):
    """Choix du plat

    Args:
        request: Requête entrante

    Context:
        dishs (list): Liste des plats ajoutés dans la
            base de données
    """
    dishs = Dish.objects.all()  # pylint: disable=maybe-no-member

    context = {
        'dishs': dishs
    }
    return render(request, 'profils/select_dish.html', context)


@login_required(login_url='connexion')
def generate_shopping_list(request, id):    # pylint: disable=redefined-builtin
    """Générer une liste de course en fonction d'un plat

    Args:
        request: Requête entrante

    Context:
        dish (int): id du plat lié à cet ingrédient
        ingredient_list (list): Liste des ingrédients contenu dans un plat
    """
    ingredient_list = IngredientList.objects.filter(  # pylint: disable=no-member
        dish=id)

    context = {
        'ingredient_list': ingredient_list,
    }
    return render(request, 'profils/generate_shopping_list.html', context)


@login_required(login_url='inscription')
def search(request):
    """Recherche d'un plat ou ingrédient

    Args:
        request: Requête entrante

    Context:
        dishs (list): Liste des plats contenant la recherche
            de l'utilisateur
        ingredients (list): Liste des plats contenant la recherche
            de l'utilisateur

    """
    query = request.GET.get('query')
    dishs = Dish.objects.filter(    # pylint: disable=no-member
        Q(name__icontains=query))
    ingredients = Ingredient.objects.filter(    # pylint: disable=no-member
        Q(name__icontains=query) | Q(name__contains=query))

    context = {
        'dishs': dishs,
        'ingredients': ingredients,
    }
    return render(request, 'profils/search.html', context)


@login_required(login_url='connexion')
def user_logout(request):
    """Déconnexion

    Args:
        request: Requête entrante
    """
    logout(request)
    return redirect('connexion')
