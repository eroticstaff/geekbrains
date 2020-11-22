class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


pos = Position("Viktor", "Yami", "Director", {"wage": 10000, "bonus": 5000})
print(pos.get_full_name())
print(pos.get_total_income())