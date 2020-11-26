class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count - other.count > 0:
            return Cell(self.count - other.count)
        else:
            raise ValueError("Клеток меньше нуля!")

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, n):
        line = ""
        for i in range(self.count // n):
            line += "*" * n
            line += "\n"
        line += "*" * (self.count % n)
        return line


cell = Cell(12)
print(cell.make_order(5))
