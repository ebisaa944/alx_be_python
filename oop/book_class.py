class Book:
    """A class representing a book with title, author, and publication year"""

    def __init__(self, title, author, year):
        """Initialize book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print message when book is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return string representation of book"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return official string representation of book"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
