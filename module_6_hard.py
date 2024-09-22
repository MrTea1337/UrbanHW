from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = bool
        self.__sides = []
        if len(sides) == 1:
            for i in range(self.sides_count):
                self.__sides.append(sides[0])
        elif len(sides) == self.sides_count:
            for side in sides:
                self.__sides.append(side)
        elif len(sides) != self.sides_count:
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        figure_color = (r, g, b)
        counter = 0
        for color in figure_color:
            if 0 <= color <= 255:
                counter += 1
        if counter == 3:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, new_sides):
        if len(new_sides) == self.sides_count:
            for side in new_sides:
                if side <= 0:
                    return
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(side for side in self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = []
            for side in new_sides:
                self.__sides.append(side)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = None

    def get_square(self):
        self.__radius = self.get_sides()[0] / (2 * pi)
        return pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = len(self) / 2
        print(len(self))
        return sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = []
        side = Figure.get_sides(self)[0]
        for i in range(self.sides_count):
            self.__sides.append(side)

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
