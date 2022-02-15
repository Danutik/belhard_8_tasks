"""
Создать 3 класса:

AmericanPerson, RussianPerson, GermanyPerson

в каждом классе определить метод i_love_science()

AmericanPerson.i_love_science() -> "I love science"
RussianPerson.i_love_science() - "Я люблю науку"
GermanyPerson.i_love_science() - "ich liebe Wissenschaft"


Написать функцию person_love_science, которая принимает объект и вызывает метод
i_love_science. Функция должна возвращать строку вида
"{obj.__class__.__name__} says that: {obj.i_love_science()}"

В блоке if __name__ == "__main__": сделать объекты трех классов и по очереди
передать их в функцию person_love_science.

https://www.youtube.com/watch?v=8o7ZKTvZpLc
"""


class AmericanPerson:
    def i_love_science(self):
        return "I love science"


class RussianPerson:
    def i_love_science(self):
        return "Я люблю науку"


class GermanyPerson:
    def i_love_science(self):
        return "ich liebe Wissenschaft"


def person_love_science(person):
    person.i_love_science()
    return f"{person.__class__.__name__} says that: {person.i_love_science()}"


if __name__ == "__main__":
    american_person = AmericanPerson()
    person_love_science(american_person)

    russian_person = RussianPerson()
    person_love_science(russian_person)

    german_person = GermanyPerson()
    person_love_science(german_person)
