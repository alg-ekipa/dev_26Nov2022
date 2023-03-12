
from typing import List, Any

class Book():
    """ Information about a book, including titile, list of authors, publkisher, ISBN and price. """
    
    def __init__(self, title: str, authors: List[str], publisher: List[str], isbn: str, price: float):
        """ Create a new book entitled title, written by the people in authors, published, publisher. """
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.isbn = isbn
        self.price = price
        
    def num_authors(self):
        """ Retrun number of authors of this book"""
        return len(self.authors)
    
python_book = Book('paractical programming', ['Campbell', 'Gries', 'Montojo'], 'Pragmatic Bookshelf', '987-1-6805026-8-8', 25.0)

print(python_book.num_authors())

