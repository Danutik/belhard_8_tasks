"""
Написать декоратор класса class_benchmark, который будет проводить
бенчмарк (замер времени выполнения) всех публичных методов класса
(те, которые не начинаются с _).

Чтобы у методов класса изменить поведение - дополнительно написать
декоратор функции def_benchmark.

До выполнения метода должен быть вывод в консоль:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода должен быть вывод в консоль:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""

import time


# start_time = time.time()
# end_time = time.time()
# difference = e - s


def class_benchmark(cls):
    functions = {
        k: v for k, v in cls.__dict__.items() if callable(v) and not k.startswith("_")
    }
    for name, func in functions.items():
        setattr(cls, name, def_benchmark(func))

    return cls


def def_benchmark(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(
            f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}\n"
            f"Время начала: {start_time}"
        )
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Выполнено {func.__name__}\n"
            f"Время окончания: {end_time}\n"
            f"Всего затрачено времени на выполнение: {end_time - start_time}"
        )
        return result

    return wrapper
