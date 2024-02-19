'=========Области видимости======='
#LEGB - local enclosed global build-in

'===========Build-in==========='
# встроенное пространство имен (list, print, dict, len, input)

'=============Global============'
# все переменные, которые мы создали внутри файла
# чтобы посмотреть все глобальные переменные, можно использовать функцию globals
# a = 10
# b = 'hello'
# print(globals())

'==============enclosed==========='
#замкнутое пространство имен - это локальное пространство, у которого есть внутреннее локальное пространство

# var = 'global' # хранится в глобальном пространстве

# def func():
#     var = 'enclosed' # замкнутое пространство
#     def inner_func():
#         var = 'local' # локальное пространство
#         print(var) # local
#     print(var) # enclosed
#     inner_func()
# print(var) # global
# func()

'===============Local============='
# локальное пространство имен - это пространство которое находится внутри функции

# a = 10
# def func():
#     global a
#     a = 20
#     print(a)
# print(a) 
# func()
# print(a)

# count = 0
# def count_():
#     global count
#     count+=1
# #     print(count)

# # count_()

# def count_(num):
#     count = 0
#     def inner_count_():
#         nonlocal count
#         count+=1
#         print(count)
#     for i in range(num):
#         inner_count_()

# count_(12)

# def func():
#     print('hello world')
#     return func

# func()()()()()

# a = 20
# a = 10

# print = 20
# print()

# def func():
#     a = 10

# print(a)

