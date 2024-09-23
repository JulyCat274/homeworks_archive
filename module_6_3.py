class Horse:
    def __init__(self, x_distance = 0, sound = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.dx = dx

class Eagle:
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.dy = dy

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        pass


    def get_pos(self): # возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance)
        pass

    def voice(self):
        pass

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

# Вывод на консоль:
# (0, 0)
# (10, 15)
# (5, 35)
# I train, eat, sleep, and repeat