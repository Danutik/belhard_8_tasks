class Person:
    name: str
    age: int
    money: int
    realty: list

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        print(f"{self.name}, {self.age}, {self.realty} и {self.money}")

    def earn_money(self, value):
        self.money += value

    def make_deal(self, house):
        difference = self.money - house.cost
        if difference >= 0:
            return self.realty.append(house)
        else:
            raise ValueError("Not enough money")
