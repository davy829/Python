import os


def upcase(s):
    return s[0].upper() + s[1:]


def show_contacts(file_name):
    os.system('cls')
    with open(file_name, 'r') as data:
        for line in data:
            print(line, end='')
    input('\npress key enter\n')


def add_contact(file_name):
    os.system('cls')
    with open(file_name, 'a') as data:
        name = ''
        name += upcase(input('Введите имя конакта_:')) + ' '
        name += upcase(input('Введите фамилию контакта_:')) + ' '
        name += upcase(input('Введите номер контакта_:'))
        res = input('Вы хотите добавить  ' + name + 'y/n')
        if res == 'y' or res == 'Y': data.write('\n' + name)
        print('Добавлено')


def find_contact(file_name):
    os.system('cls')
    what_find = input('Введите что будем искать (имя, фам, ном)_:').title()
    with open(file_name, 'r') as data:
        contacts = data.readlines()
        for cont in contacts:
            if what_find in cont:
                print(f"*{cont}")
    input('press any key')


def del_contact(file_name):
    os.system('cls')
    list_1 = []
    d1 = ''
    mystr = ''
    user_del = input('what delete? _').title()
    with open(file_name, 'r') as data:
        for item in data:
            list_1.append(item)
        for i in range(len(list_1) - 1):
            if user_del in list_1[i]:
                d1 = list_1.pop(i)
            mystr = mystr + list_1[i]
        res = input(f'You whant delete the entry {d1} y/n ...')
        if res == 'y' or res == 'Y':
            with open(file_name, 'w') as data:
                data.write(mystr)


# ----------------------------------------------------------

def upd_contact(file_name):
    os.system('cls')
    list_upd = []
    l_1 = ''
    l_2 = []
    myStr = ''
    user_change = input('what we chanch :').title()
    with open(file_name, 'r') as data:
        for item in data:
            list_upd.append(item)
        for i in range(len(list_upd) - 1):
            if user_change in list_upd[i]:
                l_1 = list_upd[i].split()
                tmp = list_upd.pop(i)
                tmpInnd = i
                for itm in l_1:
                    l_2.append(itm)
        print('1 - Меняем имя ')
        print('2 - Меняем фамилию ')
        print('3 - Меняем номер ')
        command_5 = int(input('Введите номер команды :'))
        what_change = upcase(input('Введите новое значение :'))
        os.system('cls')
        print(f'Current entry:{l_2}')
        if len(l_2) > 2:
            if command_5 == 1:
                l_2[0] = what_change
            elif command_5 == 2:
                l_2[1] = what_change
            elif command_5 == 3:
                l_2[2] = what_change
        myStr1 = ' '.join(str(y) for y in l_2)
        list_upd.insert(tmpInnd, (myStr1 + '\n'))
        myStr = ''.join(str(x) for x in list_upd)
    with open(file_name, 'w') as updateFile:
        updateFile.write(myStr)


def del_win():
    print('windows is deleted')


def interface_cont():
    os.system('cls')
    print('1 - смотреть все записи')
    print('2 - нати запись по (имени,фамилии,номеру)')
    print('3 - добавить новую запись')
    print('4 - удалить запись')
    print('5 - изменить запись')
    print('6 - выйти с программы')
    print('7 - если хотите удалить Windows ')


def main_prog(file_name):
    while True:
        os.system('cls')
        interface_cont()
        user_input = int(input('Введите номер команды от 1 до 7 : '))

        if user_input == 1:
            show_contacts(file_name)
        elif user_input == 2:
            find_contact(file_name)
        elif user_input == 3:
            add_contact(file_name)
        elif user_input == 4:
            del_contact(file_name)
        elif user_input == 5:
            upd_contact(file_name)
        elif user_input == 6:
            print('Досвиданья :)')
            return
        elif user_input == 7:
            del_win()


main_prog('test.txt')
