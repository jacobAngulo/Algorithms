#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = 0
    keys = recipe.keys()
    while True:
        has_ingredients = True
        for i in keys:
            if i in ingredients.keys() and recipe[f'{i}'] <= ingredients[f'{i}']:
                ingredients[f'{i}'] = ingredients[f'{i}'] - recipe[f'{i}']
            else:
                has_ingredients = False
        if has_ingredients:
            batches += 1
        else:
            break

    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
