class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(self.title, "пишет...")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(self.title, "рисует...")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(self.title, "чертит...")


pen = Pen("Ручка")
pen.draw()
pencil = Pencil("Карандаш")
pencil.draw()
marker = Handle("Маркер")
marker.draw()
