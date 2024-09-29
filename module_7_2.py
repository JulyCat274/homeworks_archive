def custom_write(file_name, strings):
    file_name = 'test.txt'
    strings = []


        #return result {strings_positions key:(<номер строки>, <байт начала строки>) value:записываемая строка}

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')
# Как выглядит файл после запуска:
