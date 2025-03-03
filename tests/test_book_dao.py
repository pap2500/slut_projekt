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

#Metod som kollar att det finns tre böcker

    def test_get_all_books (self): 
        books = self.databas.get_all_books ()
        assert 3 == len (books)  #För att verifiera att det är 3 böcker 

    def test_insert_book (self):
        new_book = Book ('The Hunger Games', 'J', 'Suzanne Collins') 
        self.databas.insert_book (new_book)
        books = self.databas.get_all_books ()
        assert 4 == len (books)
    
    def teardown_method(self):
        self.databas.clear_table()
        self.databas.close()