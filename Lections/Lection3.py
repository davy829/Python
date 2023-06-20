def fib(n):
    if n in [0,1]:
        return n
    return fib(n - 1) + fib(n - 2)


list_1 = []
for i in range(1,15):
    list_1.append(fib(i))
print(list_1)