import doctest

class WebSite:
    """
    Базовый класс веб-сайта

    Пример свойства getter для атрибута name:
    >>> web_site = WebSite('ВКонтакте')
    >>> name = web_site.name
    >>> print(name)
    ВКонтакте
    """
    def __init__(self, name: str, articles = 0):
        """
        Инициализация экземпляра класса.

        :param name: Название сайта.
        :param articles: Количество статей, загруженных на сайт.

        Пример:
        >>> web_site = WebSite('ВКонтакте') #инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название сайта должно быть строкой")
        if not isinstance(articles, int):
            raise TypeError("Количество статей должно быть целым")
        if articles < 0:
            raise TypeError("Количество статей должно быть не отрицательным")
        self._name = name
        self.articles = articles

    def __str__(self):
        """
        Определение поведения магического метода __str__.

        :return: Строка, предназначенная для чтения людьми.

        Пример:
        >>> web_site = WebSite('ВКонтакте')
        >>> print(web_site)
        Сайт ВКонтакте
        """
        return f'Сайт {self._name}'

    def __repr__(self):
        """
        Определение поведения магического метода __repr__.

        :return: Строка, показывающая, как может быть инициализирован экземпляр.

        Пример:
        >>> web_site = WebSite('ВКонтакте')
        >>> print(f'{web_site!r}')
        WebSite(name='ВКонтакте', articles=0)
        """
        return f'{self.__class__.__name__}(name={self._name!r}, articles={self.articles!r})'

    def access(self):
        """
        Метод, который определяет возможно ли получить доступ к сайту.

        Пример:
        >>> web_site = WebSite('ВКонтакте')
        >>> web_site.access()
        Вы получили доступ к сайту ВКонтакте
        """
        print(f'Вы получили доступ к сайту {self._name}')

    def new_article(self):
        """
        Метод, который позволяет "загрузить" новую статью (увеличение количества статей на 1).

        Пример:
        >>> web_site = WebSite('ВКонтакте')
        >>> print(web_site.articles)
        0
        >>> web_site.new_article()
        >>> print(web_site.articles)
        1
        """
        self.articles += 1

    @property
    def name(self):
        """
         Возвращает название сайта.
         Пользователь не может менять названеи сайта, поэтому атрибут name непубличный.

        :return: Название сайта.
        """
        return self._name


class PrivateSite(WebSite):
    """
    Дочерний класс приватного веб-сайта.
    """
    def __init__(self, name: str, right_password: str, articles = 0):
        """
        Инициализация экземпляра класса.
        Конструктор базового класса расширен, т.к. в дочернем классе больше аргументов, чем в базовом классе.

        :param name: Название класса.
        :param right_password: Пароль, с помощью которого можно получить доступ к сайту.
        :param articles: Количество статей, загруженных на сайт.

        Пример:
        >>> web_site = PrivateSite('ВКонтакте', 'пароль') #инициализация экземпляра класса
        """
        super().__init__(name, articles)
        if not isinstance(right_password, str):
            raise TypeError("Пароль должен быть строкой")
        self.right_password = right_password

    def __repr__(self):
        """
        Определение поведения магического метода __repr__.
        Метод был перегружен, т.к. в дочернем классе больше аргументов, чем в базовом классе.

        :return: Строка, показывающая, как может быть инициализирован экземпляр.

        Пример:
        >>> web_site = PrivateSite('ВКонтакте', 'пароль')
        >>> print(f'{web_site!r}')
        PrivateSite(name='ВКонтакте', right_password='пароль', articles = 0)
        """
        return f'{self.__class__.__name__}(name={self._name!r}, ' \
               f'right_password={self.right_password!r}, ' \
               f'articles = {self.articles!r})'

    def access(self, password: str):
        """
        Метод, который определяет возможно ли получить доступ к сайту.
        Метод был перегружен, т.к. к приватному сайту доступ можно получить только по паролю.

        :param password: Пароль, который ввел пользователью.

        Пример:
        >>> web_site = PrivateSite('ВКонтакте', 'пароль')
        >>> web_site.access('паролль')
        Пароль не верный!
        >>> web_site.access('пароль')
        Пароль верный! Вы получили доступ к сайту ВКонтакте
        """
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        if password == self.right_password:
            print(f'Пароль верный! Вы получили доступ к сайту {self._name}')
        else:
            print(f'Пароль не верный!')


if __name__ == "__main__":
    doctest.testmod()

