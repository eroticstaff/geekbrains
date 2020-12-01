class Complex:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __add__(self, other):
        return Complex(self.real + other.real, self.im + other.im)

    def __mul__(self, other):
        # (a + bi)(c + di) = ac - bd + bci + adi
        real = self.real * other.real - self.im * other.im
        im = self.im * other.real + self.real * other.im
        return Complex(real, im)

    def __str__(self):
        return f"{self.real} + {self.im}i"


a = Complex(1, 2)
print("a =", a)
b = Complex(2, 3)
print("b =", b)
c = a + b
print("a + b =", c)
print("a * b =", a * b)