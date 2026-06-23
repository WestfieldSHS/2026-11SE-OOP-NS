class Eats:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class drink(Eats):
    def __init__(self, name, price):
        super().__init__(name, price)

class food(Eats):
    def __init__(self, name, price):
        super().__init__(name, price)

class ingredient:
    def __init__(self, name):
        self.name = name    

class menu:
    def __init__(self):
        self.drinks = []
        self.food = []

    def add_drink(self, drink):
        self.drinks.append(drink)

    def add_food(self, food):
        self.food.append(food)

    def display_menu(self):
        print("Cafe Menu")
        print("\nDrinks:")
        for drink in self.drinks:
            print(f"{drink.name}: ${drink.price:.2f}")
        print("\nFood:")
        for food in self.food:
            print(f"{food.name}: ${food.price:.2f}")

    def get_ingredients(self, item_name):
        if item_name in ingredients:
            return ingredients[item_name]
        else:
            return "Item not found in menu."
        
    

# Example usage
if __name__ == "__main__":
    menu = menu()
    menu.add_drink(drink("Matcha Latte", 4.50))
    menu.add_drink(drink("Chai Tea", 3.75))
    menu.add_drink(drink("Espresso", 3.50))
    menu.add_drink(drink("Iced Coffee", 4.00))
    menu.add_drink(drink("Hot Chocolate", 3.25))
    menu.add_food(food("Croissant", 2.50))
    menu.add_food(food("Muffin", 3.00))
    menu.add_food(food("Chicken Wrap", 5.00))
    menu.add_food(food("Tuna melt", 5.50))
    menu.add_food(food("Breakfast Burrito", 6.50))
    menu.display_menu()

# Output:
# Cafe Menu
# Drinks:
# Matcha Latte: $4.50
# Chai Tea: $3.75
# Espresso: $3.50
# Iced Coffee: $4.00
# Hot Chocolate: $3.25
# Food:
# Croissant: $2.50
# Muffin: $3.00
# Chicken Wrap: $5.00
# Tuna melt: $5.50
# Breakfast Burrito: $6.50 

#Ingredients for each menu item can be retrieved using the get_ingredients method. For example:
# print(menu.get_ingredients("Matcha Latte"))
# Output: ['matcha powder', 'milk', 'sugar']

# Ingredients for each menu item


ingredients = {
    "Matcha Latte": ["matcha powder", "milk", "sugar"],
    "Chai Tea": ["black tea", "milk", "spices", "sugar"],
    "Espresso": ["coffee beans", "water"],
    "Iced Coffee": ["coffee", "ice", "milk", "sugar"],
    "Hot Chocolate": ["cocoa powder", "milk", "sugar"],
    "Croissant": ["flour", "butter", "yeast", "sugar"],
    "Muffin": ["flour", "sugar", "eggs", "milk", "baking powder"],
    "Chicken Wrap": ["tortilla", "chicken", "lettuce", "tomato", "sauce"],
    "Tuna melt": ["bread", "tuna", "cheese", "mayonnaise"],
    "Breakfast Burrito": ["tortilla", "eggs", "bacon", "cheese", "potatoes"]
}

