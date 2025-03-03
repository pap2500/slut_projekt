import pytest
from book import Book
from book_dao import BookDAO

class TestBookDAO:
    def setup_method(self):
        self.databas = BookDAO('books.db')
        books = [{'title': 'Harry Potter', 'description': 'D', 'author': 'G'},
                 {'title': 'Percy Jackson', 'description': 'E', 'author': 'H'},
                 {'title': 'Eldens Hemlighet', 'description': 'F', 'author': 'I'}]
        
        for book in books:
            new_book = Book(book['title'], book['description'], book['author'])
            self.databas.insert_book(new_book)
    
    def test_delete_book(self):
        the_book = self.databas.find_by_title('Eldens Hemlighet')
        self.databas.delete_book(the_book)
        the_book = self.databas.find_by_title('Eldens Hemlighet')
        assert the_book == None
    
    def teardown_method(self):
        self.databas.clear_table()
        self.databas.close()