BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """
    Документация на класс.
    Класс описывает модель книги.
    """
    def __init__(self, id_, name, pages):
        """
        Инициализация экземпляра класса.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Определение поведения магического метода __str__.

        :return: Строка, предназначенная для чтения людьми.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Определение поведения магического метода __repr__.

        :return: Строка, показывающая, как может быть инициализирован экземпляр.
        """
        return (f'{type(self).__name__}(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})')

# TODO написать класс Library
class Library:
    """
    Документация на класс.
    Класс описывает модель библиотеки.
    """
    def __init__(self, books=[]):
        """
        Инициализация экземпляра класса.

        :param books: Список книг.
        """
        self.books = books

    def get_next_book_id(self):
        """
        Получение идентификатора для добавления новой книги.

        :return: Идентификатор для добавления новой книги в библиотеку.
        """
        if self.books == []:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id (self, b_id):
        """
        Нахождение индекса книги из библиотеки.

        :param b_id: Идентификатор искомой книги.
        :return: Индекс искомой книги.

        :raise ValueError: Если книги с запрашиваемым id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == b_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

    def __repr__(self) -> str:
        """
        Определение поведения магического метода __repr__.

        :return: Строка, показывающая, как может быть инициализирован экземпляр.
        """
        return (f'{type(self).__name__}(books={self.books!r})')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

