try:
    from colorama import Fore, Back, Style, init
    init()
except Exception:
    # Fallbacks if colorama is not installed
    class _FG:
        RED = ''
        BLUE = ''
        GREEN = ''
        RESET = ''

    class _ST:
        RESET_ALL = ''

    Fore = _FG()
    Style = _ST()

# simple mapping from name to Fore constant
color_map = {
    'red': getattr(Fore, 'RED', ''),
    'blue': getattr(Fore, 'BLUE', ''),
    'green': getattr(Fore, 'GREEN', ''),
}

class Shape:
    x = 0
    y = 0 
    colour = ""

    def get_area(self):
        """Calculate the area of the shape and return the value"""
        pass

    def get_perimeter(self):
        """Calculate the perimeter of the shape and return the value"""
        pass
    
    def draw(self):
        """Draw the shape on the screen using the position, size and colour"""
        pass    

# Square class

class Square:
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.length = length
        self.color = color_map.get(str(color).lower(), '')

    def get_area(self):
        return self.length * self.length

    def get_perimeter(self):
        return self.length * 4

    def draw(self):
        for i in range(self.length):
            print(self.color + " " * self.length)



Square1 = Square(0, 0, 5, "red")
print(Square1.get_area())
print(Square1.get_perimeter())
Square1.draw()
print()


Square2 = Square(0, 0, 10, "blue")
print(Square2.get_area())
print(Square2.get_perimeter())
Square2.draw()
print()

Square3 = Square(0, 0, 15, "green")
print(f'Area: {Square3.get_area()}')
print(f'Perimeter: {Square3.get_perimeter()}')
Square3.draw()
print()


# Rectangle class


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color_map.get(str(color).lower(), '')

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        for i in range(self.height):
            print(self.color + " " * self.width)




Rectangle1 = Rectangle(0, 0, 5, 3, "red")
print(f'Area: {Rectangle1.get_area()}')
print(f'Perimeter: {Rectangle1.get_perimeter()}')
Rectangle1.draw()
print()

Rectangle2 = Rectangle(0, 0, 10, 5, "blue")
print(f'Area: {Rectangle2.get_area()}')
print(f'Perimeter: {Rectangle2.get_perimeter()}')
Rectangle2.draw()
print()

Rectangle3 = Rectangle(0, 0, 15, 10, "green")
print(f'Area: {Rectangle3.get_area()}')
print(f'Perimeter: {Rectangle3.get_perimeter()}')
Rectangle3.draw()
print()

# Circle class
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color_map.get(str(color).lower(), '')

    def get_area(self):
        return 3.14 * self.radius * self.radius
    
    def get_circumference(self):
        return 2 * 3.14 * self.radius
    def draw(self):
        for i in range(self.radius * 2):
            print(self.color + " " * (self.radius * 2))

Circle1 = Circle(0, 0, 5, "red")
print(f'Area: {Circle1.get_area()}')
print(f'Circumference: {Circle1.get_circumference()}')
Circle1.draw()
print()

Circle2 = Circle(0, 0, 10, "blue")
print(f'Area: {Circle2.get_area()}')
print(f'Circumference: {Circle2.get_circumference()}')
Circle2.draw()
print()

Circle3 = Circle(0, 0, 15, "green")
print(f'Area: {Circle3.get_area()}')
print(f'Circumference: {Circle3.get_circumference()}')
Circle3.draw()
print()
 
# Triangle Class
class Triangle:
    def __init__(self, x, y, base, height, color):
        self.x = x
        self.y = y
        self.base = base
        self.height = height
        self.color = color_map.get(str(color).lower(), '')

    def get_area(self):
        return 0.5 * self.base * self.height
    
    def get_perimeter(self):
        return self.base + self.height + ((self.base ** 2 + self.height ** 2) ** 0.5)
    def draw(self):
        for i in range(self.height):
            print(self.color + " " * (self.base * (i + 1) // self.height))