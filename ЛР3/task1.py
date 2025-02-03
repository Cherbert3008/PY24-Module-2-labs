import doctest

class Book:
    """ Базовый класс книги.

    Пример свойства getter для атрибута name:
    >>> book = Book('Капитанская дочка', 'А.С.Пушкин')
    >>> name = book.name
    >>> print(name)
    Капитанская дочка

    Пример свойства getter для атрибута author:
    >>> book = Book('Капитанская дочка', 'А.С.Пушкин')
    >>> author = book.author
    >>> print(author)
    А.С.Пушкин
    """
    def __init__(self, name: str, author: str):
        """
        Инициализация экземпляра класса.

        :param name: Название книги.
        :param author: Автор книги.

        Пример:
        >>> book = Book('Капитанская дочка', 'А.С.Пушкин') #инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        self._name = name
        self._author = author

    def __str__(self):
        """
        Определение поведения магического метода __str__.

        :return: Строка, предназначенная для чтения людьми.

        Пример:
        >>> book = Book('Капитанская дочка', 'А.С.Пушкин')
        >>> print(book)
        Книга Капитанская дочка. Автор А.С.Пушкин
        """
        return f'Книга {self.name}. Автор {self.author}'

    def __repr__(self):
        """
        Определение поведения магического метода __repr__.

        :return: Строка, показывающая, как может быть инициализирован экземпляр.

        Пример:
        >>> book = Book('Капитанская дочка', 'А.С.Пушкин')
        >>> print(f'{book!r}')
        Book(name='Капитанская дочка', author='А.С.Пушкин')
        """
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r})'

    @property
    def name(self):
        """
        Возвращает название книги.

        :return: Название книги.
        """
        return self._name

    @property
    def author(self):
        """
        Возвращает автора книги.

        :return: Автор книги.
        """
        return self._author


class PaperBook (Book):
    """
    Дочерний класс книги.
    Класс описывает модель бумажной книги.

    Пример свойства getter для атрибута pages:
    >>> paper_book = PaperBook('Капитанская дочка', 'А.С.Пушкин', 300)
    >>> pages = paper_book.pages
    >>> print(pages)
    300

    Пример свойства setter для атрибута pages:
    >>> paper_book = PaperBook('Капитанская дочка', 'А.С.Пушкин', 300)
    >>> paper_book.pages = 400
    >>> print(paper_book.pages)
    400
    """
    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация экзампляра класса.

        :param name: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц книги.

        Пример:
        >>> paper_book = PaperBook('Капитанская дочка', 'А.С.Пушкин', 300) #инициализация экземпляра класса
        """
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        """"
        Определение поведения магического метода __repr__.

        :return: Строка, показывающая, как может быть инициализирован экземпляр.

        Пример:
        >>> paper_book = PaperBook('Капитанская дочка', 'А.С.Пушкин', 300)
        >>> print(f'{paper_book!r}')
        PaperBook(name='Капитанская дочка', author='А.С.Пушкин', pages=300)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        """
        Возвращает количество страниц в книге.

        :return: Количество страниц в книге.
        """
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        """
        Присваивает новое количество страниц книге.

        :param new_pages: Новое количество страниц.

        :raise TypeError: Если новое количество страниц имеет не тип int, вызываем ошибку.
        :raise ValueError: Если новое количество страниц не положительное, вызываем ошибку.
        """
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook (Book):
    """
    Дочерний класс книги.
    Класс описывает модель аудио книги.

    Пример свойства getter для атрибута duration:
    >>> audio_book = AudioBook('Капитанская дочка', 'А.С.Пушкин', 3.6)
    >>> duration = audio_book.duration
    >>> print(duration)
    3.6

    Пример свойства setter для атрибута duration:
    >>> audio_book = AudioBook('Капитанская дочка', 'А.С.Пушкин', 3.6)
    >>> audio_book.duration = 4.5
    >>> print(audio_book.duration)
    4.5
    """
    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация экземпляра класса

        :param name: Название книги.
        :param author: Автор книги.
        :param duration: Продолжительность книги.

        Пример:
        >>> audio_book = AudioBook('Капитанская дочка', 'А.С.Пушкин', 3.6) #инициализация экземпляра класса
        """
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        """"
        Определение поведения магического метода __repr__.

        :return: Строка, показывающая, как может быть инициализирован экземпляр.

        Пример:
        >>> audio_book = AudioBook('Капитанская дочка', 'А.С.Пушкин', 3.6)
        >>> print(f'{audio_book!r}')
        AudioBook(name='Капитанская дочка', author='А.С.Пушкин', duration=3.6)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        """
        Возвращает длительность книги.

        :return: Длительность книги.
        """
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        """
        Присваивает новую длительность книге.

        :param new_duration: Новая длительность.

        :raise TypeError: Если новая длительность имеет не тип float, вызываем ошибку.
        :raise ValueError: Если новая длительность не положительная, вызываем ошибку.
        """
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration


if __name__ == "__main__":
    doctest.testmod()

