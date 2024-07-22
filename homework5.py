immutable_var = 0, 3, 'пять', True
print(immutable_var)

# назначение для элемента кортежа не поддерживается
#immutable_var[2] = 'шесть'
#print(immutable_var)

mutable_list = ['июнь', 'июль', 'август', 18, 385]
print(mutable_list)
mutable_list[2] = 'сентябрь'
mutable_list[4] = 'ноябрь'
mutable_list.append(100)
mutable_list.extend('200')
mutable_list.extend([200])
print(mutable_list)

mutable_list.remove('ноябрь')
print(mutable_list)