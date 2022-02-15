"""
Написать логгирующий декоратор log_decorator, который будет логгировать
вызов функции. До выполнения функции необходимо вывести в консоль строку
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}". А после вывести
строку "Выполнено {func.__name__}".

Написать логгирующий метакласс LogMeta, который ко всем методам класса добавляет
функционал декоратора log_decorator.
"""
from functools import wraps


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        return result

    return wrapper


class LogMeta(type):
    def __new__(mcs, name, bases, attrs):
        functions = {
            k: v for k, v in attrs.items() if callable(v) and not k.startswith("_")
        }
        new_class = super().__new__(mcs, name, bases, attrs)
        for name, func in functions.items():
            setattr(new_class, name, log_decorator(func))

        return new_class


class A(metaclass=LogMeta):
    def hi(self):
        print("jnfk")


if __name__ == '__main__':
    a = A()
    a.hi()
