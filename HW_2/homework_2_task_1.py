# Задача-1: Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_int = 5
my_float = 1.2
my_str = 'Maxitos'
my_list = ['hello', '2']
my_tuple = ('b', '3')
my_dict = {'tree': 'topol', 'city': 'Odessa', 'country': 'Ukraine'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')