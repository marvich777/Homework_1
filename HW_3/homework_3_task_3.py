# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

num_1 = int(input('Enter number_1: '))
num_2 = int(input('Enter number_2: '))
num_3 = int(input('Enter number_3: '))
def my_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))
my_func(num_1, num_2, num_3)