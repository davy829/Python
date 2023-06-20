import random
#
file_name = 'Степан Иван Елена Наталья Анастасия Александр Данил Юлия Мария Кирилл Ливия Ольга Андрей Анатолий'
list_2 = []
list_2 = file_name.split()
#
#
list_1 = []
finalDict = list()
for i in range(150):
    ra_num = random.randint(10, 25)
    list_1.append(ra_num)
my_set = sorted(set(list_1), key=list_1.index)




#d = {str(a + 1) + list_2:a for a in range(5)}
d = {}
for a in range(14):
    k=str(my_set[a])+' '
    d[k] = list_2[a]

for item in d:
   print('{}:{}'.format(item,d[item]))
print('-------------------')
sorted_rooms = dict(sorted(d.items()))
for item in sorted_rooms:
   print('{}:{}'.format(item,sorted_rooms[item]))
