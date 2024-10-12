def custom_write(file_name, strings):
    strings_positions = dict()
    string_count = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        string_count += 1
        key = (string_count, file.tell())
        value = string
        strings_positions[key] = value
        file.write(f'{string}\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
