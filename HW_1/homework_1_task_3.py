# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
perem = input('Vvedite chislo: ')
a = int(perem)
b = int(perem*2)
c = int(perem*3)
result = a+b+c
print(result)