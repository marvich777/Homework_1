# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты
# и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
perem = int(input('Vvedite sekundu: '))
h = perem//3600
min = perem-h*3600
min_2 = min//60
sec = min-min_2*60
vremya = f"{h:02}:{min_2:02}:{sec:02}"
print(vremya)