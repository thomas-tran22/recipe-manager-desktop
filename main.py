import tkinter as tk
from tkinter import NSEW, scrolledtext
import recipes as r


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        window = self
        recipes = r.recipeList
        tk.Tk.__init__(window, *args, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Set the window title
        window.wm_title("Recipe Manager")

        # Create a container
        container = tk.Frame(window, height=800, width=1200)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        container.configure(bg="grey")
        container.grid(row=0, column=0, sticky="nsew")

        # Create a dictionary of frames
        window.frames = {}
        for F in (MainPage, NewRecipe):
            frame = F(container, window, recipes)
            window.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        window.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, window, recipes):
        tk.Frame.__init__(self, parent)
        frame = self

        # Top Level Config

        # Make Widgets
        label = tk.Label(frame, text="Main Page")

        switch_window_button = tk.Button(
            self,
            text="Add a new Recipe?",
            command=lambda: window.show_frame(NewRecipe),
        )

        # Setting up Grid
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        # Placing Widgets
        frame.configure(background="grey")
        label.configure(bg="grey", fg="white")
        switch_window_button.configure(font=('calibre', 16))

        label.grid(row=0, column=0, padx=10, pady=10)
        switch_window_button.grid(row=1, column=0, sticky="sew")


class NewRecipe(tk.Frame):
    def __init__(self, parent, window, recipes):
        tk.Frame.__init__(self, parent)
        frame = self

        # variables
        name_var = tk.StringVar()

        # functions
        def submit():
            name = name_var.get()
            ingredients = ingr_entry.get('1.0', 'end')
            newRecipe = r.recipe(name, ingredients)
            recipes.addRecipe(recipes, newRecipe)
            print(recipes.recipes[0] if len(
                recipes.recipes) > 0 else "List is empty")

            # test
            recipeDisplay = newRecipe.getDisplay(self)
            # PLACE INTO GRID

            # zero out
            name_var.set("")

        # Create widgets

        # form for a new Recipe

        name_label = tk.Label(frame, text='Recipe Name')
        name_entry = tk.Entry(frame, textvariable=name_var)
        ingr_label = tk.Label(frame, text='Ingredients')
        ingr_entry = scrolledtext.ScrolledText(
            frame, wrap=tk.WORD, width=40, height=8, font=('calibre', 16), padx="3px")

        back_button = tk.Button(
            self,
            text="Back",
            command=lambda: window.show_frame(MainPage),
        )

        switch_window_button = tk.Button(
            self,
            text="Submit",
            command=submit
        )

        # Set up the Grid
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        frame.rowconfigure(0, weight=0)
        frame.rowconfigure(1, weight=0)
        frame.rowconfigure(2, weight=0)
        frame.rowconfigure(3, weight=0)
        frame.rowconfigure(4, weight=0)
        frame.rowconfigure(5, weight=0)

        # Place into Grid

        name_label.grid(row=0, column=0, columnspan=3)
        name_entry.grid(row=1, column=0, columnspan=3)
        ingr_label.grid(row=2, column=0, columnspan=3)
        ingr_entry.grid(row=3, column=0, padx=15, pady=6, columnspan=3)
        back_button.grid(row=4, column=0, padx=6, pady=6, sticky="se")
        switch_window_button.grid(row=4, column=2, padx=6, pady=6, sticky="sw")

        # Configure
        frame.configure(background="grey")
        name_label.configure(bg="grey", fg="white", font=('calibre', 20))
        ingr_label.configure(bg="grey", fg="white", font=('calibre', 20))
        name_entry.configure(font=('calibre', 16))


if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()
