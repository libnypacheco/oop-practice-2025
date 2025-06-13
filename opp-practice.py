# 1. Warm-up

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"
    
    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

## write tests for the Point2D class

def test_point2d():
    ptA = Point2D(1, 2)
    ptB = Point2D(4, 6)

    assert ptA.distance_to(ptB) == 5.0
    assert ptA.distance_to(ptA) == 0.0
    assert ptB.distance_to(ptB) == 0.0

test_point2d()
print("Point2D tests passed!")

# 2. Shapes in 2D
class Rectangle:
    def __init__(self, lower_left: Point2D, width, height):
        self.lower_left = lower_left
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def upper_right(self):
        return Point2D(self.lower_left.x + self.width, self.lower_left.y + self.height)

## validate that width and height are positive numbers using @property setters that raise ValueError if not.

@property
def width(self):
    return self._width

@width.setter
def width(self, value):
    if value <= 0:
        raise ValueError("Width must be positive")
    self._width = value

@property
def height(self):
    return self._height

@height.setter
def height(self, value):
    if value <= 0:
        raise ValueError("Height must be positive")
    self._height = value

## Write tests for the Rectangle class
def test_rectangle():
    lower_left = Point2D(0, 0)
    rect = Rectangle(lower_left, 3, 4)

    assert rect.area() == 12
    assert rect.perimeter() == 14
    assert rect.upper_right() == Point2D(3, 4)

    try:
        rect.width = -1
    except ValueError as e:
        assert str(e) == "Width must be positive"

    try:
        rect.height = -1
    except ValueError as e:
        assert str(e) == "Height must be positive"

test_rectangle()
print("Rectangle tests passed!")