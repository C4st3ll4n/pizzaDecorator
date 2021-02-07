from decorator.Catupiry import Catupiry
from decorator.Gorgonzola import Gorgonzola
from decorator.Mozzarela import Mozzarela
from decorator.Parmessao import Parmessao
from decorator.Pizza import Pizza
from decorator.PlainPizza import PlainPizza
from decorator.Provolone import Provolone
from decorator.TomatoSauce import TomatoSauce


def info(pizza:Pizza):
    print(f"{pizza.description}\nR${pizza.cost}")


pizza = PlainPizza()
#info(pizza)

pizza = TomatoSauce(pizza)
#info(pizza)

pizza = Mozzarela(pizza)
info(pizza)

print("\n")

cincoQueijos = Gorgonzola(Parmessao(Mozzarela(Provolone(Catupiry(TomatoSauce(PlainPizza()))))))
info(cincoQueijos)
