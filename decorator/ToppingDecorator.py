from abc import ABC

from decorator.Pizza import Pizza


class ToppingDecorator(Pizza, ABC):

    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    @property
    def description(self):
        return self.pizza.description

    @property
    def cost(self):
        return self.pizza.cost
