from decorator.Pizza import Pizza


class PlainPizza(Pizza):
    @property
    def description(self):
        return "Massa"

    @property
    def cost(self):
        return 15.00
