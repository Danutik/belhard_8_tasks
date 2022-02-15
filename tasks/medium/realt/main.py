from tasks.medium.realt.townhouse import Townhouse
from tasks.medium.realt.house import House
from tasks.medium.realt.person import Person

if __name__ == '__main__':
    house_1 = House("street, 1", 100, 1000)
    house_2 = House("street, 2", 200, 2000)
    house_3 = House("street, 3", 300, 3000)
    townhouse_1 = Townhouse("street, 1", 800)
    townhouse_2 = Townhouse("street, 2", 500)
    townhouse_3 = Townhouse("street, 3", 300)
    person_1 = Person("Igor", 25)
    person_1.earn_money(500)
    # person_1.make_deal(house_1)
    person_1.earn_money(500)
    person_1.make_deal(house_1)
