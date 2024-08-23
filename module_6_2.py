# Задача "Изменять нельзя получать"


class Vehicle:
    __COLOR_VARIANTS = ['silver', 'cherry', 'deep blue', 'uranium black', 'emerald green']

    def __init__(self,  owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        m = 'Модель:'
        return f'\n{m:<12}{self.__model:<15}'

    def get_horsepower(self):
        h = 'Мощность:'
        return f'\n{h:<12}{self.__engine_power:<15}'

    def get_color(self):
        c = 'Цвет:'
        return f'\n{c:<12}{self.__color:<15}'

    def print_info(self):
        v = 'Владелец:'
        print(self.get_model(),
              self.get_horsepower(),
              self.get_color(),
              f'\n{v:<12}{self.owner:<15}')

    def set_color(self, new_color):
        if new_color.lower() not in self.__COLOR_VARIANTS:
            print(f'\nНельзя сменить цвет на {new_color}.')
        else:
            self.__color = new_color


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


# Текущие цвета __COLOR_VARIANTS = ['silver', 'cherry', 'deep blue', 'uranium black', 'emerald green']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'deep blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('CHERRY')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
