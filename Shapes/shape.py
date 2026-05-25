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

    class Square(Shape):
        def __init__(self, x, y, length, colour):
            self.x = x
            self.y = y
            self.length = length
            self.colour = colour
        def get_area(self):
            return self.length * self.length

class Circle(Shape):
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
    def get_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
    def get_area(self):
        return self.length * self.length