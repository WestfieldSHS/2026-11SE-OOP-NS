class drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class snack:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class menu:
    def __init__(self):
        self.drinks = []
        self.snacks = []

    def add_drink(self, drink):
        self.drinks.append(drink)

    def add_snack(self, snack):
        self.snacks.append(snack)

    def display_menu(self):
        print("Cafe Menu")
        print("\nDrinks:")
        for drink in self.drinks:
            print(f"{drink.name}: ${drink.price:.2f}")
        print("\nSnacks:")
        for snack in self.snacks:
            print(f"{snack.name}: ${snack.price:.2f}")

# Example usage
if __name__ == "__main__":
    menu = menu()
    menu.add_drink(drink("Matcha Latte", 4.50))
    menu.add_drink(drink("Chai Tea", 3.75))
    menu.add_drink(drink("Espresso", 3.50))
    menu.add_drink(drink("Iced Coffee", 4.00))
    menu.add_drink(drink("Hot Chocolate", 3.25))
    menu.add_snack(snack("Croissant", 2.50))
    menu.add_snack(snack("Muffin", 3.00))
    menu.add_snack(snack("Chicken Wrap", 5.00)) 
    menu.add_snack(snack("Tuna melt", 5.50))
    menu.add_snack(snack("Breakfast Burrito", 6.50))
    menu.display_menu()




