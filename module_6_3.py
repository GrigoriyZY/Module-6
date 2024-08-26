# Задача "Мифическое наследование"

class Horse:
    """Базовый класс - Лошадь"""
    def __init__(self):
        super().__init__()
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        """Функция для расчета перемещения по горизонтали"""
        self.x_distance = self.x_distance + dx


class Eagle:
    """Базовый класс - Орёл"""
    def __init__(self):
        super().__init__()
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        """Функция для расчета перемещения по вертикали"""
        self.y_distance = self.y_distance + dy


class Pegasus(Eagle, Horse):

    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        """Метод вычисления перемещения Пегаса"""
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        """Метод возвращает координаты Пегаса"""
        pos = self.x_distance, self.y_distance
        return pos

    def voice(self):
        """Метод возвращающий звук, издаваемый Пегасом"""
        return print(self.sound)


# Код для проверки
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
