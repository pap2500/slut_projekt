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

    def test_update_book(self, create_database):
        book = create_database.find_by_title('Percy Jackson')
        book.description = 'Ny beskrivning för Percy Jackson'
        create_database.update_book(book)
        book = create_database.find_by_title('Percy Jackson')
        assert book.description == 'Ny beskrivning för Percy Jackson'
    
    
    def test_delete_book(self, create_database):
        the_book = create_database.find_by_title('Eldens Hemlighet')
        create_database.delete_book(the_book)
        the_book = create_database.find_by_title('Eldens Hemlighet')
        assert the_book == None
        
    def test_find_by_title(self, create_database):
         #metod som hämtar en book via titel och veriferar att dess beskrivning stämmer med förväntat värde
        book = create_database.find_by_title('Harry Potter')
        assert book.description == ('D')


