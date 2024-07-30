calls = 0
def count_calls(): #подсчитывает вызовы остальных функций
    global calls
    calls += 1
def string_info(string):
    count_calls()
    string_tuple = (len(string), string.upper(), string.lower())
    return string_tuple
def is_contains(string, list_to_search):
    count_calls()
    result = False
    for item in list_to_search:
        if string.lower() in item.lower():
            result = True
    return result

print(string_info('Проспект'))
print(string_info('Деятельность'))
print(is_contains('Психология', ['холл', 'Психолог', 'психоЛОГИЯ']))
print(is_contains('атмосфера', ['атом', 'атлас']))
print(calls)