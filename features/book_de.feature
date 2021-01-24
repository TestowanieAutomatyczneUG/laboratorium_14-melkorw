# language:de
Funktionalität: Managing books in database
  @atrapa
  Szenario: We can get all books
    Gegeben sei we have mocked database
    Wenn two books are in database
    Dann we can get all books

  Szenario: We cannot get book
    Gegeben sei we have database
    Wenn have id not being integer
    Dann item does not exist, error

  Szenariogrundriss: Getting book title
    Gegeben sei we have mocked database with mocked method returning <book>
    Wenn we give id equal to <book_id>
    Dann Returned book title should be equal to <title>

    Beispiele:
   | book   | book_id                 | title                 |
   | {"title": "title_test_0", "author": {"name": "name", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}   | 0  | title_test_0 |
   | {"title": "title_test_1", "author": {"name": "name", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}   | 1 | title_test_1 |
   | {"title": "title_test_2", "author": {"name": "name", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}   | 2  | title_test_2 |