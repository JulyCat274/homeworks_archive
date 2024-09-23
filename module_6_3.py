class Horse:
    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.dx = dx
        if dx > 0:
            x_distance = self.x_distance + self.dx
            return x_distance


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.dy = dy
        if dy > 0:
            y_distance = self.y_distance + self.dy
            return y_distance
class Pegasus(Horse, Eagle):
    def __init__(self, x_distance, y_distance, sound):
        Horse.__init__(self, x_distance)
        Eagle.__init__(self, y_distance)
        super().__init__(sound)
    def move(self, dx, dy):
        pass


    def get_pos(self): # возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance)
        pass

    def voice(self):
        pass


p1 = Pegasus()

print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())

p1.voice()

# Вывод на консоль:
# (0, 0)
# (10, 15)
# (5, 35)
# I train, eat, sleep, and repeat