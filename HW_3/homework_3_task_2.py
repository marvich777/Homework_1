# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name_1 = input('Enter name: ')
surname_1 = input('Enter surname: ')
year_1 = int(input('Enter year of born: '))
city_1 = input('Enter city of born: ')
email_1 = input('Enter your e-mail: ')
telefon_1 = int(input('Enter your telefone: '))

def imen_arg (name, surname, year, city, email, telefon):
    print(f"name - {name_1}; surname - {surname_1}; year - {year_1}; city - {city_1}; email - {email_1}; telefon - {telefon_1}")
imen_arg(name =name_1, surname=surname_1, year=year_1, city=city_1, email=email_1, telefon=telefon_1)