from django.shortcuts import render, redirect
from .models import Recipe, Author
from random import sample
from .forms import RecipeForm


def index(request):
    random_recipes = sample(list(Recipe.objects.all()), k=3)
    context = {'random_list': random_recipes}
    return render(request, 'myapp/main.html', context=context)


# Create your views here.
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            author = Author(name=request.user)
            author.save()
            recipe = Recipe(name=cd['name'], description=cd['description'], stages=cd['stages'],
                            time=cd['time'], image=cd['image'], category=cd['category'],
                            author=author)
            recipe.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'myapp/add_recipe.html', {'form': form})


def show_all(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'myapp/show_all.html', context=context)
