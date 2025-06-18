class Book:
    """
    A class representing a book with title, author, and publication year.
    Implements magic methods for object initialization, string representation,
    and cleanup.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a Book instance.

        Args:
            title: The book's title (non-empty string)
            author: The book's author (non-empty string)
            year: The publication year (positive integer)
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the book is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Return an unambiguous representation for developers."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
