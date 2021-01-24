from abc import ABC


class BookRepository(ABC):
    def __init__(self, data_source=[]):
        self.__data_source = data_source

    def find_all(self):
        return self.data_source

    def find_by_id(self, book_id):
        return self.data_source[book_id]

    def add(self, book):
        self.__data_source.append(book)
        return True

    def delete(self, book):
        self.__data_source.remove(book)
        return True

    @property
    def data_source(self):
        return self.__data_source
