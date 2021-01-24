from behave import *
import json
from unittest.mock import *
from book.BookService import BookService
from book.BookRepository import BookRepository
use_step_matcher("re")

@step("Mamy bazę danych")
def step_impl(context):
    context.repo = BookRepository()
    context.service = BookService(context.repo)

@step("Mamy książkę")
def step_impl(context):
    context.book = {"title": "title_test", "author": {"name": "name", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}


@step("Można dodać ją i usunąć z bazy")
def step_impl(context):
    assert context.service.add_book(context.book)
    assert len(context.repo.data_source) == 1
    assert context.service.delete_book(0)
    assert len(context.repo.data_source) == 0

@step("Mamy zamockowana bazę danych")
def step_impl(context):
    repo = Mock(BookRepository())
    repo.find_by_id.return_value = {"title": "title_test", "author": {"name": "name", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}
    context.repo = repo
    context.service = BookService(context.repo)

@step("Mamy id ksiazki")
def step_impl(context):
    context.book_id = 0

@step("Można pobrac ja z bazy")
def step_impl(context):
    assert context.service.get_book(context.book_id) == {"title": "title_test", "author": {"name": "name", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}

@step("we have mocked database")
def step_impl(context):
    repo = Mock(BookRepository())
    context.repo = repo
    context.service = BookService(context.repo)

@step("two books are in database")
def step_impl(context):
    context.repo.find_all.return_value = [{"title": "title_test_2", "author": {"name": "name", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}, {"title": "title_test", "author": {"name": "name", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}]

@step("we can get all books")
def step_impl(context):
    assert context.service.get_books() == [{"title": "title_test_2", "author": {"name": "name", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}, {"title": "title_test", "author": {"name": "name", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}]

@step("we have database")
def step_impl(context):
    context.repo = BookRepository()
    context.service = BookService(context.repo)

@step("have id not being integer")
def step_impl(context):
    context.book_id = 'id'

@step("item does not exist, error")
def step_impl(context):
    assert context.service.get_book(context.book_id) == 'Book Error'

@step("we have mocked database with mocked method returning (?P<book>.+)")
def step_impl(context, book):
    repo = Mock(BookRepository())
    repo.find_by_id.return_value = json.loads(book)
    context.repo = repo
    context.service = BookService(context.repo)

@step("we give id equal to (?P<book_id>.+)")
def step_impl(context, book_id):
    context.book_id = int(book_id)

@step("Returned book title should be equal to (?P<title>.+)")
def step_impl(context, title):
    assert context.service.get_book_title(context.book_id) == title

@step("Mamy zamockowana bazę danych z metoda zwracajaca (?P<ksiazka>.+)")
def step_impl(context, ksiazka):
    repo = Mock(BookRepository())
    repo.find_by_id.return_value = json.loads(ksiazka)
    context.repo = repo
    context.service = BookService(context.repo)

@step("dajemy id rowne (?P<book_id>.+)")
def step_impl(context, book_id):
    context.book_id = int(book_id)

@step("Zwracana ksiazka mam autora o imieniu (?P<imie>.+)")
def step_impl(context, imie):
    assert context.service.get_book_author_name(context.book_id) == imie