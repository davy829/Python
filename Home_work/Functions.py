def Fibo(n):  # вернет фибоначи
    if n in [0, 1]:
        return n
    else:
        return Fibo(n - 1) + Fibo(n - 2)


def Prostoe(n1):
    if n1 > 2 and n1 % 2 != 0:
        for i in range(3,n1 // 2):
            if n1 % 2 != 1:
               return 'no simple'
        return 'simle'
    return 'no simple'


def Recount(mynum):
    print(mynum, end='.')
    if mynum == 0:
        return mynum
    Recount(mynum - 1)


def sqear(num_1, num_2):
    if num_2 == 1:
        return num_1
    if num_1 != 1:
        return num_1 * sqear(num_1, num_2 - 1)


def sum_one_plus_one(num_1, num_2):
    if num_2 == 0:
        return num_1
    num_1 = num_1 + 1
    return sum_one_plus_one(num_1 , num_2 - 1)


