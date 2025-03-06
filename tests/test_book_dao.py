import pytest
from book import Book
from book_dao import BookDAO

class TestBookDAO:
    @pytest.fixture
    def create_database(self):
        databas = BookDAO('books.db')
        books = [{'title': 'Harry Potter', 'description': 'D', 'author': 'G'},
                {'title': 'Percy Jackson', 'description': 'E', 'author': 'H'},
                {'title': 'Eldens Hemlighet', 'description': 'F', 'author': 'I'}]
        
        for book in books:
            new_book = Book(book['title'], book['description'], book['author'])
            databas.insert_book(new_book)

        yield databas
        databas.clear_table()   
        databas.close()
    
    def test_update_book(self, create_database):
        book = create_database.find_by_title('Percy Jackson')
        book.description = 'Ny beskrivning för Percy Jackson'
        create_database.update_book(book)
        book = create_database.find_by_title('Percy Jackson')
        assert book.description == 'Ny beskrivning för Percy Jackson'