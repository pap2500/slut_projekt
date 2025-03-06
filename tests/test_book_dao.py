import pytest
from book import Book
from book_dao import BookDAO

class TestBookDao:
    @pytest.fixture
    def create_database(self):
        database = BookDAO("Books.db") 
        
        
        books = [{'title': 'Harry Potter', 'description': 'D', 'author': 'G'},
                 {'title': 'Percy jackson', 'description': 'E', 'author': 'H'},
                 {'title': 'Eldens Hemlighet', 'description': 'F', 'author': 'I'}]
        
        
        for book in books:
            new_book = Book(book['title'], book['description'], book['author'])
            database.insert_book(new_book)
        
        
   
    
        yield database
        database.clear_table()
        database.close()
            
            
    def test_find_by_title(self, create_database):
         #metod som hämtar en book via titel och veriferar att dess beskrivning stämmer med förväntat värde
        book = create_database.find_by_title('Harry Potter')
        assert book.description == ('D')
        
            
    
    
    
          
    