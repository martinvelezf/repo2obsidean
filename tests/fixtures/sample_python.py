"""Sample Python module for testing."""


class MyClass:
    """A simple class for testing."""

    def __init__(self, name: str):
        """Initialize the class."""
        self.name = name

    def greet(self):
        """Greet using the name."""
        return f"Hello, {self.name}!"

    @property
    def upper_name(self):
        """Return uppercase name."""
        return self.name.upper()


class InheritedClass(MyClass):
    """A class that inherits from MyClass."""

    def special_greet(self):
        """A special greeting."""
        result = self.greet()
        return f"Special: {result}"


def standalone_function(x: int) -> int:
    """A standalone function."""
    return x * 2


def another_function():
    """Calls another function."""
    value = standalone_function(5)
    obj = MyClass("Test")
    greeting = obj.greet()
    return value + len(greeting)
