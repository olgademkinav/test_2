from abc import ABC, abstractmethod


class Clothes(ABC):
    count = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.count += self.consumption

    def __str__(self):
        return f"Пальто: size - {self.size}, consumption -{self.consumption}, total consumption -{Coat.count}"

    @property
    def consumption(self):
        cons = (self.size) / 6.5 + 0.5
        return float(cons)


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        Costume.count += self.consumption

    def __str__(self):
        return f"Костюм: height - {self.height}, consumption - {self.consumption}, total consumption - {Costume.count}"

    @property
    def consumption(self):
        cons = (self.height) * 2 + 0.3
        return float(cons)


clothes_1 = Coat(48)
clothes_2 = Costume(174)
print(clothes_1)
print('__________________')
print(clothes_2)
