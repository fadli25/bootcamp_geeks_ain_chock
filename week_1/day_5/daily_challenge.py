import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must specify either radius or diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("Can only add another Circle.")

    # Comparison: bigger
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    # Comparison: equal
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    # Optional: allow sorting by radius
    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

# Example usage
circle1 = Circle(radius=5)
circle2 = Circle(diameter=12)

print(circle1)            # Circle(radius=5.00, diameter=10.00, area=78.54)
print(circle2)            # Circle(radius=6.00, diameter=12.00, area=113.10)

# Add circles
circle3 = circle1 + circle2
print(circle3)            # Circle(radius=11.00, diameter=22.00, area=380.13)

# Compare circles
print(circle1 > circle2)  # False
print(circle1 < circle2)  # True
print(circle1 == circle2) # False

# Sorting circles
circle_list = [circle3, circle1, circle2]
circle_list.sort()
print(circle_list)        # Sorted by radius