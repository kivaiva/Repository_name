class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def name(self):
        return self._name

    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def pages(self):
        return self._pages

    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}. Страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def duration(self):
        return self._duration

    def duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError
        self._duration = float(value)

    def __str__(self):
        return f"{super().__str__()}. Длительность: {self.duration} часов"
