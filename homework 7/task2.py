from abc import abstractmethod, ABC


class Cloth(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def price(self):
        pass


class Coat(Cloth):
    def __init__(self, name, size):
        self.V = size
        super().__init__(name)

    @property
    def price(self):
        return self.V / 6.5 + 0.5


class Suit(Cloth):
    def __init__(self, name, height):
        self.H = height
        super().__init__(name)

    @property
    def price(self):
        return self.H * 2 + 0.3


coat = Coat("Vispuchi", 100)
print(coat.price)
suit = Suit("Armanio", 300)
print(suit.price)
