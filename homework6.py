my_dict = {'Лиза': 2011, 'Маруся': 2018, 'Архип': 2013}
print(my_dict)
print(my_dict['Архип'])
print(my_dict.get('Лиза'))
print(my_dict.get('Костик', 'Такое имя отсутствует.'))
my_dict.update({'Шарик': 2017, 'Бобик': 2014})
print(my_dict)
name = my_dict.pop('Маруся')
print(my_dict)
print(name)

my_set = {1, 2, 3.14, 4, 'Sun', 'Mon', 'Wed', 'Fri', 'Mon', 'Wed', 'Sun', 1, 2, 3.14, 4}
print(my_set)
my_set.add(7)
my_set.add((98, 97, 95))
my_set.remove('Wed')
print(my_set)