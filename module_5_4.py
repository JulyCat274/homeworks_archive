class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __del__(cls, *args):
        if len(cls.houses_history) > 1:
            print(cls.houses_history[1], 'снесён, но он останется в истории')
            del cls.houses_history[1]

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)