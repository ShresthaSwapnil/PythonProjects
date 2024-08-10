# Student Name: [Aryaman Bista]
# Student ID: [E2300132]

class Recipe:
    def _init_(self, name, cuisine, ingredients, rating):
        self.name = name
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.set_rating(rating)

    def get_name(self):
        return self.name

    def get_cuisine(self):
        return self.cuisine

    def get_ingredients(self):
        return self.ingredients

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        if rating >= 0:
            self.rating = rating
        else:
            print("Rating should be a positive number.")

    def _str_(self):
        return f"{self.name} - Cuisine: {self.cuisine}, Ingredients: {', '.join(self.ingredients)}, Rating: {self.rating}"

recipes = []

def main():
    print("Welcome to Recipe Manager")
    while True:
        print("\n1. Add Recipe")
        print("2. Display All Recipes")
        print("3. Filter Recipes by Cuisine")
        print("4. Display the Highest Rated Recipe")
        print("5. Exit")

        choice = input("Kindly choose a number within the range of 1 to 5: ")

        if choice == "1":
            add_recipe()
        elif choice == "2":
            all_recipes()
        elif choice == "3":
            filter_cuisine()
        elif choice == "4":
            highest_rated()
        elif choice == "5":
            print("Thank you for using the Recipe Manager. Goodbye!")
            break
        else:
            print("The system only accepts numerical inputs (1 to 5). Please try entering a valid number.")

def add_recipe():
    name = input("Enter recipe name: ")
    while not name:
        print("Recipe name cannot be empty. Please try again.")
        name = input("Enter recipe name: ")

    cuisine = input("Enter cuisine type: ")
    while not cuisine:
        print("Cuisine type cannot be empty. Please try again.")
        cuisine = input("Enter cuisine type: ")

    ingredients = input("Enter ingredients (separated by commas): ")
    while not ingredients:
        print("Ingredients cannot be empty. Please try again.")
        ingredients = input("Enter ingredients (separated by commas): ")

    rating = input("Enter rating (out of 5): ")
    while not rating or float(rating) > 5:
        if not rating:
            print("Rating cannot be empty. Please try again.")
        elif float(rating) > 5:
            print("Rating should be less than or equal to 5. Please try again.")
        rating = input("Enter rating (out of 5): ")

    recipe = Recipe(name, cuisine, ingredients.split(","), float(rating))
    recipes.append(recipe)
def all_recipes():
    if not recipes:
        print("There are no recipes in the collection.")
    else:
        print(f"There are currently {len(recipes)} recipes in the collection:")
        for recipe in recipes:
            print(f"The current recipe in the collection:\n{recipe}")

def filter_cuisine():
    cuisine_type = input("Enter the cuisine type to filter: ")
    filtered_recipes = [recipe for recipe in recipes if recipe.get_cuisine().lower() == cuisine_type.lower()]
    if not filtered_recipes:
        print(f"No recipes found for the {cuisine_type} cuisine.")
    else:
        print(f"Recipes in the {cuisine_type} cuisine:")
        for recipe in filtered_recipes:
            print(recipe)

def highest_rated():
    if not recipes:
        print("There are no recipes in the collection.")
    else:
        highest_rating = 0
        highest_recipe = None
        for recipe in recipes:
            if recipe.get_rating() > highest_rating:
                highest_rating = recipe.get_rating()
                highest_recipe = recipe
        print(f"The highest-rated recipe is: {highest_recipe}")

try:
    main()
except:
    print(f"An error occurred: Please try again. Did you entered words instead of a number?")