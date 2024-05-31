from sets_categories_data import (ALCOHOLS)
def clean_ingredients(dish_name, dish_ingredients):
    ingredients = set(dish_ingredients)
    return (dish_name, ingredients)

def check_drinks(drink_name, drink_ingredients):
    bebidas = set(drink_ingredients)
    alcohol = bebidas.intersection(ALCOHOLS)
    if len(alcohol) != 0:
        nombre = f"{drink_name} Cocktail"
        return (nombre)
    elif len(alcohol) == 0:
        nombre = f"{drink_name} Mocktail"
        return (nombre)
