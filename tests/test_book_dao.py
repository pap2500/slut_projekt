import pytest
from book import Book
from book_dao import BookDAO

class TestBookDAO:

    @pytest.fixture 

    def create_databas (self):
        databas = BookDAO ('books.db')
        books = [{'title': 'Harry Potter', 'description': 'D', 'author': 'G'},
                 {'title': 'Percy Jackson', 'description': 'E', 'author': 'H'},
                 {'title': 'Eldens Hemlighet', 'description': 'F', 'author': 'I'}]

        for book in books:
            new_book = Book(book['title'], book['description'], book['author'])
            databas.insert_book(new_book)

        yield databas
        databas.clear_table ()
        databas.close()

        
        
#Metod som kollar att det finns tre böcker

    def test_get_all_books (self, create_databas): 
        books = create_databas.get_all_books ()
        assert 3 == len (books)  #För att verifiera att det är 3 böcker 
        
#Metod som lägger till en bok och veriferar att det är 4 böcker nu
    def test_insert_book (self, create_databas):
        new_book = Book ('The Hunger Games', 'J', 'Suzanne Collins') 
        create_databas.insert_book (new_book)
        books = create_databas.get_all_books()
        assert 4 == len (books)