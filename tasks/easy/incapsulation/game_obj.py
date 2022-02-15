"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- private атрибут x (тип int)
- private атрибут y (тип int)
- магический метод __init__, который принимает начальные x и y

Координаты должны быть доступны для чтения (сделать property), а их изменение
должно происходить в методе move(delta_x, delta_y). (изменение - это +=)
"""


class GameObject:
    __x = 0
    __y = 0

    def __init__(self, __x, __y):
        self.__x = 0
        self.__y = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def move(self, delta_x, delta_y):
        self.__x += delta_x
        self.__y += delta_y
