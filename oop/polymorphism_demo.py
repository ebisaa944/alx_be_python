import math

class Shape:
    """Base class representing a geometric shape"""
    
    def area(self):
        """Calculate the area of the shape (to be overridden by subclasses)"""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Rectangle shape that inherits from Shape"""
    
    def __init__(self, length, width):
        """
        Initialize rectangle dimensions
        
        Args:
            length (float): Length of the rectangle
            width (float): Width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate rectangle area (length × width)"""
        return self.length * self.width


class Circle(Shape):
    """Circle shape that inherits from Shape"""
    
    def __init__(self, radius):
        """
        Initialize circle radius
        
        Args:
            radius (float): Radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate circle area (π × radius²)"""
        return math.pi * (self.radius ** 2)
