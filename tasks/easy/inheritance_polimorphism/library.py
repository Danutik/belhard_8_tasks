"""
Определить класс Person:

- атрибут fullname - ФИО (тип str)
- атрибут phone - номер телефона (тип str)
- магический метод __init__, который принимает fullname и phone

Описать класс LibraryReader, который наследуется от Person:

- атрибут uid - номер читательского билета (тип int)
- атрибут books - список книг (тип set)
- магический метод __init__, который принимает fullname, phone, uid, а books
  заполняет пустым множеством
- метод take_books(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. взял(а)
  книги: Приключения, Словарь, Энциклопедия", если было взято до 3 книг
  включительно. Если было взято больше книг, то возвращает строку: "Петров В.В.
  взял(а) 4 книги".
- метод return_book(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. вернул(а)
  книги: Приключения, Словарь, Энциклопедия", если было возвращено до 3 книг
  включительно. Если было возвращено больше книг, то возвращает строку:
  "Петров В.В. вернул(а) 4 книги". Если какой-то книги нет, то бросить исключение
  ValueError с сообщением "Петров В. В. не брал: Рассказы", при этом книги не
  должны быть удалены

Названия книг в сообщениях должны быть отсортированы по алфавиту.
"""


class Person:
    fullname: str
    phone: str

    def __init__(self, fullname: str, phone: str):
        self.fullname = fullname
        self.phone = phone


class LibraryReader(Person):
    uid: int
    books: set

    def __init__(self, fullname: str, phone: str, uid: int):
        super().__init__(fullname, phone)
        self.uid = uid
        self.books = set()

    def take_books(self, *args):
        self.books.update(args)
        sort_books = ", ".join(sorted(self.books))
        if len(args) <= 3:
            return f"{self.fullname} взял(а) книги: {sort_books}"
        else:
            return f"{self.fullname} взял(а) {len(args)} книги"

    def return_book(self, *args):
        ret_sort_books = ", ".join(sorted(args))
        args = set(args)
        if self.books.issuperset(args):
            if len(args) <= 3:
                return f"{self.fullname} вернул(а) книги: {ret_sort_books}"
            else:
                return f"{self.fullname} вернул(а) {len(args)} книги"
        else:
            raise ValueError(f"{self.fullname} не брал: {args.difference(self.books)}")


if __name__ == '__main__':
    person_1 = LibraryReader("Петров Х.Г.", "375293465958", 123)
    print(person_1.take_books("Пиноккио", "Курочка-ряба", "Азбука", "Спартак"))
    print(person_1.return_book("Пиноккио", "Спартак", "Курочка-ряба"))
