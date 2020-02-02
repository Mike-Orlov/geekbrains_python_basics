"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно. 
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, 
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, brand='-=Brand=-'):
        self.brand = brand

    @abstractmethod
    def material_need(self):
        pass

class Coat(Clothes):
    def __init__(self, brand):
        super().__init__(self)

    @property
    def material_need(self):
        self.v = float(input('Enter V for your coat (V/6.5 + 0.5):\n'))
        return f'For the coat u need {self.v / 6.5 + 0.5} material\n'

class Suit(Clothes):
    def __init__(self, brand):
        Clothes.__init__(self, brand)

    @property
    def material_need(self):
        self.h = float(input('Enter H for your coat (2*H + 0.3):\n'))
        return f'For the suit u need {2 * self.h + 0.3} material\n'

coat1 = Coat('Zara')
suit1 = Suit('Bandini')
print(coat1.material_need)
print(suit1.material_need)