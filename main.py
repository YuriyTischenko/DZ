import os
import shutil

while True:

    for dirpath, dirnames,filenames in os.walk("."):
        for dirname in dirnames:
            print('Каталог:', os.path.join(dirpath, dirname))
        for filename in filenames:
            print('файл:', os.path.join(dirpath, filename))
    print ('1 - создание файла')
    print ('2 - удаление файла')
    print ('3 - перемещение файла или каталога')
    print ('4 - копирование файла')
    print ('5 - создание каталога')
    print ('6 - удаление каталога')
    print ('7 - копирование каталога')
    print ('0 - выход')
    print ('\n')
    menu = input('выберете нужный пункт меню:')

    match menu:
        case '1':
            name_file = input('Введите имя и расширение файла')
            if not(os.path.exists(name_file)):
                file = open (name_file, 'w')
            else:
                print('Такой файл уже существует!')
        case '2':
            name_file = input('Введите имя файла для удаления')
            if os.path.exists(name_file):
                os.remove(name_file)
            else:
                print('Нет такого каталога!')
        case '3':
            name_file = input('Введите имя файла или папки для переноса: ')
            name_dir = input('В какую папку переносить: ')
            if (os.path.exists(name_file)) and (
                    os.path.exists(name_dir) and (not (os.path.exists(name_dir + '/' + name_file)))):
                shutil.move(name_file, name_dir)
            else:
                print('Нет такого файла, папки или они уже есть в папке назначения!')
        case '4':
            name_file = input('Введите имя файла для копирования: ')
            name_dir = input('В какую папку копировать: ')
            if (os.path.exists(name_file)) and (os.path.exists(name_dir) and (not(os.path.exists(name_dir+'/'+name_file))) ):
                shutil.copy2(name_file, name_dir)
            else:
                print('Нет такого файла или файл уже есть в папке назначения!')
        case '5':
            name_dir = input ('Введите имя создаваемого каталога: ')
            if not (os.path.exists(name_dir)):
                os.mkdir(name_dir)
            else: print ('Такой католог уже существует!')
        case '6':
            name_dir = input('Введите имя каталога для удаления')
            if os.path.exists(name_dir):
                os.rmdir(name_dir)
            else:
                print('Нет такого каталога!')
        case '7':
            name_dir = input('Введите имя папки для копирования: ')
            name_dir_dest = input('В какую папку копировать: ')
            if (os.path.exists(name_dir)) and (
                    os.path.exists(name_dir_dest) and (not (os.path.exists(name_dir_dest + '/' + name_dir)))):
                shutil.copytree(name_dir, name_dir_dest+'/'+name_dir)
            else:
                print('Нет такого файла или файл уже есть в папке назначения!')
        case _:
            break