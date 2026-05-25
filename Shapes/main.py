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

class Square:
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.length = length
        self.color = color

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

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

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
