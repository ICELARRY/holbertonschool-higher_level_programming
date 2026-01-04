class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the string representation of the rectangle using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol_str = str(self.print_symbol)
        row = symbol_str * self.width
        return "\n".join(row for _ in range(self.height))

    def __repr__(self):
        """Return a string representation that can recreate the instance."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message and decrement the instance count on deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
