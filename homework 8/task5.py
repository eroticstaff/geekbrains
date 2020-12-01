class Storage:
    storage = {"Printers": 0, "Scanners": 0}

    def add(self, item):
        if type(item) == Printer:
            self.storage['Printers'] += 1
        elif type(item) == Scanner:
            self.storage['Scanners'] += 1


class OfficeEquipment:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight


class Printer(OfficeEquipment):
    def __init__(self, color, weight, type_of_paper):
        if type_of_paper not in ['A3', 'A4', 'A5']:
            raise ValueError("Not right type of paper!")
        self.type_of_paper = type_of_paper
        super().__init__(color, weight)

    def print_text(self, text):
        print("Printed text:", text)


class Scanner(OfficeEquipment):
    def __init__(self, color, weight, size):
        self.size = size
        super().__init__(color, weight)

    def scan(self):
        print("Scanning...")