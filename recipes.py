from cProfile import label
import tkinter as tk


class recipe():
    name = ""
    ingredients = []

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients.splitlines()

    def __str__(self):
        output = "The Recipe's Name is: " + self.name + "\n"
        output += "For this recipe you will need: \n"
        for i in self.ingredients:
            output += i + "\n"
        return output

    def getDisplay(self, window):
        # creates a container for the whole display
        display_instance = tk.Frame(window, height=200, width=300)

        # Create var
        nameVar = tk.StringVar(window, self.name)

        # Create Widget
        name_display = tk.Label(display_instance, textvariable=nameVar)

        # Place Widget
        name_display.pack()
        return display_instance


class recipeList():
    recipes = []

    def addRecipe(self, recipe):
        self.recipes.append(recipe)
