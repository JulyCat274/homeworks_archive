# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    if i > 1:
        for j in range(2, i - 1):
            if(i % j) == 0:
                not_primes.append(i)
                break
        else:
            primes.append(i)
print(primes)
print(not_primes)