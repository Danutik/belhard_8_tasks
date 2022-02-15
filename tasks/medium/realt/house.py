class House:
    address: str
    area: int
    cost: int

    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, value):
        self.cost += value
        return self.cost

    def decrease_cost(self, value):
        self.cost -= value
        return self.cost
