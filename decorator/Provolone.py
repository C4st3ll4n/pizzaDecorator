from decorator.Pizza import Pizza
from decorator.ToppingDecorator import ToppingDecorator


class Provolone(ToppingDecorator):

    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    @property
    def description(self):
        return f"{self.pizza.description}, Provolone"

    @property
    def cost(self):
        return 2.00 + self.pizza.cost