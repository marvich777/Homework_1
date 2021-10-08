# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или
# убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли
# к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

vur = int(input('Vvedite vyruchky firmy: '))
izd = int(input('Vvedite izderjki firmy: '))
result = vur-izd

if vur > izd:
    print('Pozdravlyaem! Vasha firma rabotaet s vyruchkoi)')
    print('Rentabelnost firmy sostavlyaet: ', result/vur)
else:
    print('Uvy, Vasha firma rabotaet v ubytok(')

sotr = int(input('Vvedite kolichestvo sotrudnikov firmu: '))
prib = (result/vur)/sotr
print('V raschete na odnogo sotrudnika pribyl firmu sostavlyaet: ', prib)