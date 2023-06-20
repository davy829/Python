# Задача №1
# cars = int(input('Скольк км в дeнь прoедит машина ?_'))
# dis = int(input('Сколько надо проехать км ?_'))
# res = (cars + dis - 1) // cars
# print(f"{res}  дня в пути")


 #Задача №2
# pup1 = int(input('Сколько учеников в первом классе_'))
# pup2 = int(input('Сколько учеников во втором классе_'))
# pup3 = int(input('Сколько учеников в третьем классе_'))
# res = (pup1 + pup2 + pup3 + 1) // 2
# print(f"{res}  парт надо")


 #Задача №3
# numVagFromHead = int(input('Номер вагона от головы_'))
# numVag = int(input('Порядковый номер вагона_'))
# if numVag == numVagFromHead:
#     res = 'Слишком мало данных'
# else:
#     res = numVag + numVagFromHead - 1
# print(f"{res} вагогов ")


# Задача №4
year = int(input('Введите любые четыре цифры года (2023)_'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    res = 'Это високосный год'
else:
    res = 'Это обычный год'
print(f"{res} ")