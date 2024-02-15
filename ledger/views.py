from django.shortcuts import render
from django.http import HttpResponse 


def index(request):
    return HttpResponse('Recipe Book')


def recipe_list(request):
    # paste context from here
    ctx = {
    "recipe_list": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3 pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1 pc"
                },
                {
                    "name": "pork",
                    "quantity": "1 kg"
                },
                {
                    "name": "water",
                    "quantity": "1 L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1 pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2 cup"
                },
                {
                    "name": "water",
                    "quanity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    ]
}
    return render(request, 'recipe_list.html', ctx)


def recipe1(request):
    # paste context from here
    ctx = {
    "name": "Recipe 1",
    "ingredients": [
        {
            "name": "tomato",
            "quantity": "3 pcs"
        },
        {
            "name": "onion",
            "quantity": "1 pc"
        },
        {
            "name": "pork",
            "quantity": "1 kg"
        },
        {
            "name": "water",
            "quantity": "1 L"
        },
        {
            "name": "sinigang mix",
            "quantity": "1 packet"
        }
    ],
    "link": "/recipe/1"
}
    return render(request, 'recipes.html', ctx)


def recipe2(request):
    # paste context from here
    ctx = {
    "name": "Recipe 2",
    "ingredients": [
        {
            "name": "garlic",
            "quantity": "1 head"
        },
        {
            "name": "onion",
            "quantity": "1 pc"
        },
        {
            "name": "vinegar",
            "quantity": "1/2 cup"
        },
        {
            "name": "water",
            "quantity": "1 cup"
        },
        {
            "name": "salt",
            "quantity": "1 tablespoon"
        },
        {
            "name": "whole black peppers",
            "quantity": "1 tablespoon"
        },
        {
            "name": "pork",
            "quantity": "1 kilo"
        }
    ],
    "link": "/recipe/2"
}
    return render(request, 'recipes.html', ctx)




