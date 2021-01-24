# language:vi
Tính năng: Zarządzanie książkami
  Użytkownik ma książki w systemie bazodanowym z którymi może pracować
  Tình huống: Użytkownik może dodać i usunąć książkę
    Biết Mamy bazę danych
    Khi Mamy książkę
    Thì Można dodać ją i usunąć z bazy

  @atrapa
  Tình huống: Użytkownik może pobrac ksiazke
    Biết Mamy zamockowana bazę danych
    Khi Mamy id ksiazki
    Thì Można pobrac ja z bazy

  Khung tình huống: Bierzemy imie autora
    Biết Mamy zamockowana bazę danych z metoda zwracajaca <ksiazka>
    Khi dajemy id rowne <book_id>
    Thì Zwracana ksiazka mam autora o imieniu <imie>

    Dữ liệu:
   | ksiazka   | book_id                 | imie                 |
   | {"title": "title_test_0", "author": {"name": "name1", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}   | 0  | name1 |
   | {"title": "title_test_1", "author": {"name": "name2", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}   | 1 | name2 |
   | {"title": "title_test_2", "author": {"name": "name3", "email": "email@gmail", "surname":" surname"}, "isbn": "12345678-123"}   | 2  | name3 |
