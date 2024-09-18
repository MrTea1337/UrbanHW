class Vehicle:
    owner = str()
    __model = str()
    __engine_power = int()
    __color = str()
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, __model, __color, __engine_power):
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        return f"Модель: {self.__model}\n"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}\n"

    def get_color(self):
        return f"Цвет: {self.__color}\n"

    def print_info(self):
        print(f"{self.get_model()}{self.get_horsepower()}{self.get_color()}Владелец: {self.owner}")

    def set_color(self, new_color):
        for color in self.__COLOR_VARIANTS:
            if color.lower() == new_color.lower():
                self.__color = new_color
                return
        print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, __model, __color, __engine_power):
        super().__init__(__model, __color, __engine_power)
        self.owner = owner


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Feds', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
