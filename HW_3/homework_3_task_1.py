# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

arg_1 = int(input('Vvedite 1-e chislo: '))
arg_2 = int(input('Vvedite 2-e chislo: '))

def my_delenie (arg_1, arg_2):
    if arg_2==0:
        print('Delenie na 0 nevozmojno')
    return arg_1 / arg_2
print(my_delenie(arg_1, arg_2))
