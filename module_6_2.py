class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return 'Модель: ' + self.__model

    def get_horsepower(self):
        return f'Мощность двигателя:  {self.__engine_power}'

    def get_color(self):
        return 'Цвет: ' + self.__color

    def print_info(self):
        print(Sedan.get_model(self))
        print(Sedan.get_horsepower(self))
        print(Sedan.get_color(self))
        print('Владелец:', self.owner)

    def set_color(self, new_color):
        new_color = str(new_color)
        if new_color.lower() not in self.__COLOR_VARIANTS:
            print('Нельзя сменить цвет на ' + new_color)
        else:
            self.__color = new_color
            return self.__color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
