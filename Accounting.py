import json

def ff(func):
    while loop:
        func()
        cont = input('Желаете внести еще изменения?')
        if cont == 'Да':
            continue
        else:
            print('Последний список:')
            sorti()

            break


def main():
    print('Программа учета')
    print('Команды')
    print('1)Просмотреть список')
    print('2)Добавить новый элемент')
    print('3)Просмотреть количество')
    print('4)Увеличить количество')
    print('5)Уменьшить количество ')
    print('6)Exit')
    global command
    command = int(input('Введите номер команды'))

loop = True
try:
    file = open('data.json', 'r')
    prod = file.read()  # {'огурцы': 1, 'молоко': 2} str
    prod_dict = eval(prod)
except FileNotFoundError:
    print('Добро пожаловать в программу учета!\nВы можете создать свой первый список')
while loop:
    try:
        main()


        def new():
            element = input('Ведите наименование продукта')
            quantity = int(input('Введите количетсво'))
            prod_dict[element] = quantity
            sorti()


        def how():
            element = input('Введите наименование')
            if element not in prod_dict.keys:
                print('Такого элемента нету в списке')
            else:
                quantity = prod_dict[element]
                print('Количеcтво', \
                      element, \
                      'равно',
                      quantity)


        def plus():
            element = input('Введите наименование')
            if element not in prod.keys():
                print('Такого элемента нету в списке')
            else:
                plus = int(input('Введите на сколько увечилось'))
                prod_dict[element] += plus
                sorti()
            # key_error(element)


        def minus():
            element = input('Введите наименование')
            if element not in prod.keys():
                print('Такого элемента нету в списке')
            else:
                minus = int(input('Введите на сколько уменьшить'))
                prod_dict[element] -= minus
                sorti()
            # key_error(element)


        def sorti():
            #print('---------------------{}'.format(type(prod_dict)))
            #print('---------------------{}'.format(prod_dict))
            for key in sorted(prod_dict):
                print(key, ':', prod_dict[key])


        if command == 1:
            sorti()


        elif command == 2:
            ff(new)
        elif command == 3:
            ff(how)
        elif command == 4:
           ff(plus)
        elif command == 5:
            ff(minus)
        elif command == 1:
            sorti()
        elif command == 6:
            file.close()
            with open('data.json', 'w') as file:
                json.dump(prod_dict, file, indent=2, ensure_ascii=False)
            print('Good Bye')
            loop = False
        else:
            print('Error:Неправильно введена команда')
            # main()

    except ValueError:
        print('Вводить нужно цифры!!!')
