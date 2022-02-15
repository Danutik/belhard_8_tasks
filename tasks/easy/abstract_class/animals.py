"""
Описать абстрактный класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:

- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def says(self):
        pass


class Cat(Animal):

    def __init__(self, name=""):
        super().__init__(name)

    def says(self):
        super().says()
        return f"{self.name} - кошка. Говорит МЯУ!"


class Dog(Animal):

    def __init__(self, name=""):
        super().__init__(name)

    def says(self):
        super().says()
        return f"{self.name} - собака. Говорит ГАВ!"


class Cow(Animal):

    def __init__(self, name=""):
        super().__init__(name)

    def says(self):
        super().says()
        return f"{self.name} - корова. Говорит МУ!"


if __name__ == '__main__':
    a = Cat()
    a.says()

    b = Dog("Шарик")
    b.says()

    c = Cow("Милка")
    c.says()
