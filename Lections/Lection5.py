def sqear(num_1, num_2):
    return num_1 * num_2


# s = "1 2 3 5 8 15 23 38"
# list_1 = s.split()
# list_res = []
# res = [int(item) for item in list_1]
# for i in range(len(res)):
#     if res[i] % 2 == 0:
#         mv = sqear(res[i], res[i])
#         list_res.append(f"{res[i]};{mv}")
# print(*list_res)

data = (1, 2, 3, 5, 8, 15, 23, 38)
res = list()
for i in data:
    if i % 2 == 0:
        res.append((i, i ** 2))
print(res)
