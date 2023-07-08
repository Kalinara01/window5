'''Файлы. Работа с файлами'''

# open(путь до файла/название файла, режим) - функия которя позваляет отркывать файлы и работать с ними
# file = open('/home/test/Desctop/test.py') - абсолютный путь
# file = open('test.py') - относительный путь


'''Режимы'''
# 1.r(read) - открывает файл для чтения.
# Указатель ставится в самое начало.Режим по умолчанию, если такого файла нет, то прозойдет ошибка

# file = open('test.py')
# file = open('files.py', 'r')

# 2. w(write) - Открывает файл для записи. Перезаписывается содержимое файла. Если нет такого файла, то создаст пустой файл с таким название
# file = open('test.py', 'w')

# # 3. a(append) - открывает файл добавления. Указатель в конце, если файл нет - создаст
# file = open('test.py', 'a')

# 4. x(exclusive) - создает уникальный файл

# 5. t(text) - Открывает файл в текстовом видею Режиме по умолчанию

# 6. b(binary) - Открывает файл в бинаром виде
# rb - чтение в бинарном виде
# wb - запись в бинарном виде
# ab - дозапись в бинарном виде

# 7. + >- Открывает файл как в режиме чтения, так и в режиме записи
# r+
# w+

'''Методы режима r'''
# 1. read() - если параметр не указан, то чтение до конца файла
# 2. readLine() - считывает только одну строку за раз -> str
# 3. readLines() - считывает все строки файла -> list

# #read
# file = open('test.py')
# data = file.read()
# # print(data)
# print(file.tell()) # возвращает индекс, где находится указатель
# file.close()# файл обяхательно нужно закрывать

# # file.seek(int) - перемещает указать на указанный int

# readline
# file =  open('test.py', 'rt')
# data = file.readline()
# data2 = file.readline()
# print(data, data2)
# file.close()

# f = open('test.py', 'rt')
# for line in f:
#     print(line)

# f.close()

# f = open('test.py')
# print(f.readlines())
# f.close()

'''Методы режима w'''
# 1. write('string')
# 2. writlines(list)

# f = open('test2.py', 'w')
# # f.write('py27 hello')
# # f.writelines(['hello\n', 'world'])
# f.writelines({'a': '2'}) - только ключи принимает
# f.close()

# try:
#     f = open('test.py', 'r')
#     ...
# finally:
#     f.close()
#     print(f.close)

'''Контекстный менеджер - Открывает файл и при любом раскладе будет закрывать файл'''
# with open('test.py')as f:
#     print(f)

# r+
# with open('test.py', 'r+') as f:
#     f.write('12434565768 mode r+')
#     f.seek(0)
#     print(f.read())

# w+
# with open('test.py', 'w+') as f:
#     f.write('12434565768 mode w+')
#     f.seek(0)
#     print(f.read())


# x+ >- создвет файл с уникальным 
# with open('test3.py', 'x+') as f:
#     # print(f)
#     f.writelines(['q\n', 'a'])
#     f.seek(0)
#     print(f.readlines())

# # a+
# with open('test.py', 'a+') as f:
#     f.write('new str')
#     f.seek(0)
#     print(f.readlines)



'''JSON, Модули и пакеты'''
'''
JavaScrip object Notation - Единый текстовый формат передачи и хранения данных между приложенияЮ языкоами программирования, frontend - backend
'''
{
   "id": 1,
   "author": "John",
#    "post": null

}

'''Разница'''
#python                      JSON
# dict                         object
# list                         Array
# tuple                        Array
# str                          String
# int                          Number
# float                        Number
# True                         true
# False                        false
# None                         null

import json

# Сериализация(Запись данный в JSON) - перевод Python объекта в JSON
# dump - метод записывает Python объект в JSON файл (файл в формате JSON)
# dumps - метод считвает Python объект и переводит в строку в формат JSON

# Десириализация (чтение данных из JSON) - переводит JSON в Python объект

# load - cчитываем файл в формате JSON и переводит в Python объект
# loads - считывает текст в формате JSON и переводит в Python объект

import json

# json.loads(json_object)
# person = '{"name": "Jonh", "age": 25}'
# result = json.loads(person)
# print(result)

# json.load(file)

# with open('test.json', 'w+') as file:
#     person = '{"name": "Jonh", "age": 25}'
#     file.write(person)
#     file.seek(0)
#     data = json.loa(file)
#     print(data.get('name'))

# json.dumps(python_object)

# person = {"name": "Jonh", "age": 25, 'have_car': False}
# print(json.dumps(person))


# with open('test.json', 'w+') as file:
#     json.dump(person,file)
#     print(file.read())
   
# import package_
# print(dir(package_))

# from package_ import file_module
# print(dir(file_module))

# from package_.file_module import sum_file

# from package_ import file_module as f

# # f.sum_file()
# # f.read_sum_file()

# import random as rand
# rand.choice()

'''import'''
# import module_name as псевдоним

# from модуль/пакет import ... [as псевдоним]


# from паакет1.пакет2юпакет3 import модуль
# from паакет1.пакет2юпакет3 модуль import
# функция, переменная ...

# from .module.name import ...

# from package_ import hello импортируем модуль
# print(hello.hello)

# from package_ import file_module

# file_module.sum_file(4, 67)
# print(type(file_module.read_sum_file()))

# from package_.my_package import file1
# file1.print2()


#  дз CSV