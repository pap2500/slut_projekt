import pytest
from book import Book
from book_dao import BookDAO

class TestBookDAO:
    def setup_method(self):
        self.databas = BookDAO('Books.db')
        books = [{'title': 'A', 'description': 'D', 'author': 'G'},
                 {'title': 'B', 'description': 'E', 'author': 'H'},
                 {'title': 'C', 'description': 'F', 'author': 'I'}]
        
        for book in books:
            new_book = Book(book['title'], book['description'], book['author'])
            databas.insert_book(new_book)