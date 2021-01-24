from abc import ABC


class BookService(ABC):
    def __init__(self, book_repository=None):
        self.book_repository = book_repository

    def get_books(self):
        return self.book_repository.find_all()

    def get_book(self, book_id):
        if type(book_id) is not int or book_id < 0:
            return 'Book Error'
        if self.book_repository.find_by_id(book_id):
            return self.book_repository.find_by_id(book_id)
        else:
            return 'Item does not exist'

    def get_book_title(self, book_id):
        if type(book_id) is not int or book_id < 0:
            return 'Book Error'
        if self.book_repository.find_by_id(book_id):
            book = self.book_repository.find_by_id(book_id)
            return book['title']
        else:
            return 'Item does not exist'

    def get_book_author_name(self, book_id):
        if type(book_id) is not int or book_id < 0:
            return 'Book Error'
        if self.book_repository.find_by_id(book_id):
            book = self.book_repository.find_by_id(book_id)
            return book['author']['name']
        else:
            return 'Item does not exist'

    def add_book(self, book):
        return self.book_repository.add(book)

    def delete_book(self, book_id):
        if type(book_id) is not int or book_id < 0:
            return 'Book Error'
        if self.book_repository.find_by_id(book_id):
            self.book_repository.delete(self.book_repository.find_by_id(book_id))
            return True
        return False
