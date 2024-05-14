from django.urls import path
from .views import index, add_recipe, show_all

urlpatterns = [
    path('', index, name='index'),
    path('add_recipe', add_recipe, name='add_recipe'),
    path('show_all', show_all, name='show_all')
]
