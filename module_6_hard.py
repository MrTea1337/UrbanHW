class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__color = list(color)
        self.filled = bool
        self.__sides = []
        for i in range(self.sides_count):
            self.__sides.append(sides)

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
        return self.__sides[0] * self.sides_count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = []
            for side in new_sides:
                self.__sides.append(side)


class Circle(Figure):
    sides_count = 1
    __radius = int

    def get_square(self, len_=0, radius=0):
        pass


class Triangle(Figure):
    sides_count = 3

    def get_square(self, a, b, c):
        pass


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        pass


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
