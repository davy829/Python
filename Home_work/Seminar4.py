# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
# ---------------------РЕШЕНИЕ----------------------------------------------------
# text_1 = '2 4 6 8 10 12 10 8 6 4 2'
# text_2 = '3 6 9 12 15 18'
# set_1 = set(text_1.split())
# set_2 = set(text_2.split())
# res_1 = set_1.intersection(set_2)
# print('In text repeat is : ', end=f' ')
# print(*res_1)
# -----------------------------------------------------------------------------------

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.

# ---------------------РЕШЕНИЕ----------------------------------------------------
count_bush = int(input('How match bushes of blueberries_: '))
max_count_berries = 0
count_berries_three_bush = 0
count_berries_one_bush = []
for i in range(count_bush):
    count_berries_one_bush.insert(i, input('How match berries on the bush_: '))
print(*count_berries_one_bush)
for i in range(count_bush-1):
    current_bush_prev = count_berries_one_bush[i - 1]
    current_bush = count_berries_one_bush[i]
    current_bush_next = count_berries_one_bush[i+1]
    res_1 = int(current_bush_prev) + int(current_bush) + int(current_bush_next)
    if res_1 > max_count_berries:
        max_count_berries = res_1
        res_2 = current_bush_prev + current_bush + current_bush_next
print(f"Maximal berries is {res_2} their is a {max_count_berries} berries")