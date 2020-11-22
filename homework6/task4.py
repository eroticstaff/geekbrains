class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car is going...")

    def stop(self):
        print("Car stopped.")

    def turn(self, direction):
        print(f"Car turned {direction}")

    def show_speed(self):
        print(f"Current speed is {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Speed limit!!!")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Speed limit!!!")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

town_car = TownCar(70, "red", "Jiguli", False)
sport_car = SportCar(120, "blue", "BMW", False)
work_car = WorkCar(30, "white", "Audi", False)
police_car = PoliceCar(70, "black", "BMW", True)
town_car.show_speed()
police_car.go()
