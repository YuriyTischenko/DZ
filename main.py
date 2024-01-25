import os
while True:
    print (*os.listdir())
    print ('1 - создание файла')
    print ('2 - удаление файла')
    print ('3 - перемещение файла')
    print ('4 - копирование файла')
    print ('5 - создание каталога')
    print ('6 - удаление каталога')
    print ('7 - перемещение каталога')
    print ('8 - копирование каталога')
    print ('0 - выход')
    print ('\n')
    menu = input('выберете нужный пункт меню:')

    match menu:
        case '1':
            print(menu)
        case '2':
            print(menu)
        case '3':
            print(menu)
        case '4':
            print(menu)
        case '5':
            print(menu)
        case '6':
            print(menu)
        case '7':
            print(menu)
        case _:
            break