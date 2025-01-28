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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__

