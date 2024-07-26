my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_index = 0
my_list_max_index = (len(my_list))
while my_list_index < my_list_max_index:
    if my_list[my_list_index] > 0:
        print(my_list[my_list_index])
    my_list_index = my_list_index + 1