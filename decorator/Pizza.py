from abc import ABC


class Pizza(ABC):
    @property
    def description(self):
        return None

    @property
    def cost(self):
        return None
