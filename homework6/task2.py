class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_mass(self):
        return self.__width * self.__length * 5 * 25


new_road = Road(100, 10)
print(new_road.calculate_mass())
