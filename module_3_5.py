def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    other_digits = int(str_number[1:])
    if len(str(other_digits)) > 1:
        return first * get_multiplied_digits(other_digits)
    else:
        return first * other_digits


result = get_multiplied_digits(40203)
print(result)
