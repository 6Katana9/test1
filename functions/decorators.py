# # '======Функция высшего порядка===='
# # # функция высшего порядка - это функция которая принимает в аргументы другую функцию, создает внутри себя другую функцию, вызывает функцию и возвращает функцию

# # # def func1():
# # #     return 'hi'

# # # def func2(func_):
# # #     print(func_())

# # # func2(func1)

# # '==========Декораторы=========='
# # # декораторы - это функции высшего порядка, которая нужна для расширения функционала другой функции не изменяя ее (функция оберток)

# # # def decorator_glushitel(a):
# # #     def wrapper():
# # #         text = a()
# # #         res = 'тихо ' + text # тихо стрелять
# # #         print(res)
# # #     return wrapper 

# # # def gun():
# # #     return 'стрелять'
# # # def gun2():
# # #     return 'стрелять'

# # # wrapper = decorator_glushitel(gun)
# # # wrapper() # способ использовать декоратор в ручную


# # '-----------------------------------'
# # # def decorator_glushitel(func):
# # #     def wrapper():
# # #         text = func()
# # #         res = 'тихо ' + text
# # #         print(res)
# # #     return wrapper 

# # # @decorator_glushitel
# # # def gun():
# # #     return 'стрелять'

# # # gun() # способ использовать декоратор при помощи синтаксического сахара

# # '-------------------------------------'
# # from datetime import datetime

# # # def decorator(func):
# # #     def wrapper():
# # #         print('start:', datetime.now())
# # #         func()
# # #         print('finish:', datetime.now())
# # #     return wrapper

# # # @decorator
# # # def hello():
# # #     print('hello world')

# # # hello()


# # '------------------------------------------'
# # # def func_start_time(func):
# # #     def wrapper(*args, **kwargs):
# # #         print('start:', datetime.now())
# # #         func(*args, **kwargs)
# # #     return wrapper

# # # @func_start_time
# # # def sum_(a, b):
# # #     print(a + b)

# # # sum_(20, 10)
# # '------------------------------------------'
# # def decorator(num):
# #     def inner_decorator(func):
# #         def wrapper(*args, **kwargs):
# #             for i in range(num):
# #                 func(*args, **kwargs)
# #         return wrapper
# #     return inner_decorator

# # @decorator(10)
# # def hello():
# #     print('hello world')

# # # hello()
# # '-------------------------------------------'
# # # адание 1Напишите декоратор call_function, который печатает перед вызовом полученной функции строку:
# # #  Вызываю функцию <имя_функции>

# # # Затем следует вызов функции. После вызова функции должна печататься строка:
# # #  "Вызов функции <имя_функции> прошёл успешно"

# # # Ввод:
# # # @call_function
# # # def first():
# # #     print("hello world")
# # #     return "hello world"
# # # first()

# # # Вывод:
# # # Вызываю функцию first
# # # hello world 
# # # Вызов функции first прошёл успешно


# # def call_function(func):
# #     def wrapper(*args, **kwargs):
# #         print('Вызываю функцию', func.__name__)
# #         func(*args, **kwargs)
# #         print('Вызов функции', func.__name__, 'прошёл успешно')
# #     return wrapper


# # @call_function
# # def first():
# #     print("hello world")
# #     return "hello world"

# # first()

# # a = 20 
# # for i in range(5):
# #     while i < 3:
# #        i += 1
# #        a += 1

# # print(a)


