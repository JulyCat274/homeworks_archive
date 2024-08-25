class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        current_floor = 0
        for current_floor in range(0, self.number_of_floors):
            if new_floor < 1 or new_floor > self.number_of_floors:
                print('Такого этажа не существует')
                break
            elif new_floor > current_floor:
                current_floor += 1
                print(current_floor)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Кошкин дом', 3)
h1.go_to(5)
h2.go_to(10)
h3.go_to(2)
