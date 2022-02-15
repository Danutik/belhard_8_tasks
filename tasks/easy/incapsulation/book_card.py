"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""

from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    author: str
    title: str
    year: int

    def __init__(self, author: str, title: str, year: int):
        self.__author = author
        self.__title = title
        self.__year = year

    def __eq__(self, other):
        return self.__year == other

    def __lt__(self, other):
        return self.__year < other

    def __le__(self, other):
        return self.__year <= other

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if isinstance(author, str):
            self.__author = author
        else:
            raise ValueError

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self.__title = title
        else:
            raise ValueError

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int) and year > 0 and year <= CURRENT_YEAR:
            self.__year = year
        else:
            raise ValueError


if __name__ == '__main__':
    gh = BookCard()
    # gh.year = 2111
    # print(gh.year)
    # gh.title = 123
    # print(gh.title)
    gh.year = -15
    print(gh.year)
