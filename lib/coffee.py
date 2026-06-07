#!/usr/bin/env python3

class Coffee:
    pass

    def __init__(self, size: str, price: float):
        """
        Initializes a Coffee instance.
        :param size: The sizing token string (Small, Medium, or Large).
        :param price: The initial cost float representation of the coffee.
        """
        # Trigger validation property on initialization
        self.size = size
        self.price = price

    @property
    def size(self) -> str:
        """Getter for the coffee size attribute."""
        return self._size

    @size.setter
    def size(self, value):
        """Ensures the coffee size input matches allowed menu options."""
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
            self._size = "Medium" # Sensible fallback default
        else:
            self._size = value

    def tip(self):
        """Validates experience satisfaction, printing appreciation and incrementing cost."""
        print("This coffee is great, here’s a tip!")
        self.price += 1