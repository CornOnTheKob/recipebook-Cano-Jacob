from django.urls import path
from .views import index, recipe_list, recipe1, recipe2

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipe/1', recipe1, name="recipe 1"),
    path('recipe/2', recipe2, name="recipe 2"),
]

app_name = "ledger"
