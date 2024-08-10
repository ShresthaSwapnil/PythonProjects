class Recipe:
    def __init__(self, name, cuisine, ingredients, rating):
        # Initializes a Recipe object with the given parameters.
        self.name = name
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.rating = rating

    def get_name(self):
        # Returns the name of the recipe.
        return self.name

    def get_cuisine(self):
        # Returns the cuisine type of the recipe.
        return self.cuisine

    def get_ingredients(self):
        # Returns the list of ingredients required for the recipe.
        return self.ingredients

    def get_rating(self):
        # Returns the rating of the recipe.
        return self.rating

    def set_rating(self, rating):
        # Sets the rating of the recipe if it's a non-negative value.
        if rating >= 0:
            self.rating = rating
        else:
            print("Rating must be a non-negative value.")

    def __str__(self):
        # Returns a string representation of the recipe.
        return f"{self.name} - Cuisine: {self.cuisine}, Ingredients: {', '.join(self.ingredients)}, Rating: {self.rating}"


def main():
    # The main entry point of the Recipe Manager application.
    recipe_collection = []
    while True:
        print("\nWelcome To Recipe Manager")
        print("1. Add Recipe")
        print("2. Display All Recipes")
        print("3. Filter Recipes by Cuisine")
        print("4. Display the Highest Rated Recipe")
        print("5. Exit")

        try:
            option = int(input("Kindly choose a number within the range of 1 to 5: "))
        except ValueError:
            print("The system only accepts numerical inputs. Please try entering a valid number.")
            continue

        if option == 1:
            add_recipe(recipe_collection)
        elif option == 2:
            all_recipes(recipe_collection)
        elif option == 3:
            filter_cuisine(recipe_collection)
        elif option == 4:
            highest_rated(recipe_collection)
        elif option == 5:
            print("\nThank you for using the Recipe Manager. Goodbye!")
            break
        else:
            print("The system only accepts numerical inputs within the range of 1 to 5. Please try again.")


def add_recipe(recipe_collection):
    # Adds a new recipe to the collection.
    name = input("Enter recipe name: ")
    cuisine = input("Enter cuisine type: ")
    ingredients = input("Enter ingredients (separated by commas): ").split(',')
    rating = 0
    while rating <= 0 or rating > 5:
        try:
            rating = float(input("Enter rating (out of 5): "))
            if rating < 0 or rating > 5:
                print("Rating must be a numerical value between 0 and 5.")
        except ValueError:
            print("Rating must be a numerical value.")
    recipe_collection.append(Recipe(name, cuisine, ingredients, rating))


def all_recipes(recipe_collection):
    # Displays all recipes in the collection.
    if len(recipe_collection) == 0:
        print("There are currently no recipes in the collection.")
    else:
        print("There are currently " + str(len(recipe_collection)) + " recipes in the collection:")
        for recipe in recipe_collection:
            print(recipe)


def filter_cuisine(recipe_collection):
    # Filters recipes by cuisine type.
    cuisine_type = input("Enter the cuisine type to filter: ")
    matching_recipes = [recipe for recipe in recipe_collection if recipe.get_cuisine() == cuisine_type]
    if len(matching_recipes) == 0:
        print("There are currently no recipes in the " + cuisine_type + " cuisine.")
    else:
        print("Recipes in the " + cuisine_type + " cuisine:")
        for recipe in matching_recipes:
            print(recipe)


def highest_rated(recipe_collection):
    # Displays the highest-rated recipe in the collection.
    if not recipe_collection:
        print("There are no recipes in the collection.")
        return

    highest_rated_recipe = max(recipe_collection, key=lambda recipe: recipe.rating)
    print(f"The highest-rated recipe is: {highest_rated_recipe.name}, Cuisine: {highest_rated_recipe.cuisine}, Rating: {highest_rated_recipe.rating}")

if __name__ == "__main__":
    main()