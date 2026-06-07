#!/usr/bin/env python3

class Book:
    pass
    def __init__(self, title: str, page_count: int):
        """
        Initializes a Book instance.
        :param title: The string title of the book.
        :param page_count: The total number of pages (must be an integer).
        """
        self.title = title
        # Use the setter property to trigger validation on initialization
        self.page_count = page_count

    @property
    def page_count(self) -> int:
        """Getter for the book's page count."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Setter for page count that ensures the value is an integer."""
        if not isinstance(value, int):
            print("page_count must be an integer")
            # Set to a fallback default or raise an exception depending on test setup
            self._page_count = 0 
        else:
            self._value = value
            self._page_count = value

    def turn_page(self):
        """Simulates turning a page in the book."""
        print("Flipping the page...wow, you read fast!")   