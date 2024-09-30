def custom_write(file_name, strings):
    strings_count = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        strings_count += 1
        strings = (strings_count, file.tell())
        file.write(f'{string}\n')
        my_dict = {strings:string}
        print(my_dict)
    file.close()
    file = open(file_name, 'r', encoding='utf-8')
    result = file.read()
    file.close()



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
