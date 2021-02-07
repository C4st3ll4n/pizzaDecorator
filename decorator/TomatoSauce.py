from decorator.Pizza import Pizza
from decorator.ToppingDecorator import ToppingDecorator


class TomatoSauce(ToppingDecorator):

    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    @property
    def description(self):
        return f"{self.pizza.description}, Molho de tomate"

    @property
    def cost(self):
        return 3.00 + self.pizza.cost