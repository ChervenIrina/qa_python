import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тест1: проверяем add_new_book(). Нельзя добавить книги с названием более 40 символов (41 и 44 символ)
    @pytest.mark.parametrize('book', ['Тайны прошлого: Исследователь в забвении.', 'Мир чудес и забав: Путишествие в страну снов'])
    def test_not_add_new_book_more_max_characters(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)

        assert collector.get_books_genre() == {}

    # тест2: проверяем add_new_book(). Книги с одинаковым названием добавить можно один раз
    def test_add_double_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 1

    # тест3: проверяем set_book_genre() + get_books_with_specific_genre(). Добавляем корректный жанр к сущ.книге
    def test_add_genre_exist_book(self):
        book = 'Девушка с татуировкой дракона'
        genre = 'Детективы'
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_books_with_specific_genre(genre)[0] == book

    # тест4: проверяем set_book_genre() + get_book_genre() + get_books_genre(). Добавляем корректный жанр к не сущ.книге
    def test_add_genre_not_exist_book(self):
        book = 'Девушка с татуировкой дракона'
        genre = 'Детективы'
        collector = BooksCollector()
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) not in collector.get_books_genre().values()

    # тест5: проверяем set_book_genre() и get_books_with_specific_genre(). Добавляем не корректный жанр к сущ.книге
    def test_add_not_genre_exist_book(self):
        book = 'Я робот'
        genre = 'Роман'
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_books_with_specific_genre(genre) == []

    # тест6: проверяем get_books_for_children(). Добавляем книгу, которая не соответствует genre_age_rating, но ссответствует genre
    def test_add_new_book_for_children(self):
        book = 'Приключения Незнайки и его друзей'
        genre = 'Мультфильмы'
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_books_for_children() == [book]

    # тест7: проверяем get_books_for_children(). Добавляем книги, которые соответствует genre_age_rating или нет в genre
    @pytest.mark.parametrize('book, genre', [['Девушка с татуировкой дракона', 'Детективы'],
                                      ['Эмиль и Марго: Монстры повсюду!', 'Комиксы']])
    def test_add_new_book_not_for_children(self, book, genre):
        collector = BooksCollector()
        collector.set_book_genre(book, genre)

        assert collector.get_books_for_children() == []

    # тест8: проверяем add_book_in_favorites(). Добавляем сущ.книгу в избранные
    def test_add_book_in_favorites(self):
        book = 'Приключения Незнайки и его друзей'
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert collector.get_list_of_favorites_books()[0] == book

    # тест9: проверяем add_book_in_favorites(). Добавляем дубль сущ.книгу в избранные
    def test_add_double_book_in_favorites(self):
        book = 'Приключения Незнайки и его друзей'
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert len(collector.get_list_of_favorites_books()) == 1

    # тест10: проверяем add_book_in_favorites(). Добавляем не сущ.книгу в избранные
    def test_add_not_exist_book_in_favorites(self):
        book = 'Приключения Незнайки и его друзей'
        collector = BooksCollector()
        collector.add_book_in_favorites(book)

        assert len(collector.get_list_of_favorites_books()) == 0

    # тест11: проверяем delete_book_from_favorites(). Удаляем сущ.книгу из избранных
    def test_delete_book_in_favorites(self):
        book = 'Приключения Незнайки и его друзей'
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert len(collector.get_list_of_favorites_books()) == 0

    # тест12: проверяем delete_book_from_favorites(). Удаляем не сущ.книгу из избранных
    def test_delete_not_exist_book_in_favorites(self):
        book = 'Приключения Незнайки и его друзей'
        collector = BooksCollector()
        collector.delete_book_from_favorites(book)

        assert len(collector.get_list_of_favorites_books()) == 0
