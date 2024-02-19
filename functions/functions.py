# # '===========Функция==========='
# # # функция - это именнованный блок кода, который может принимать аргументы и возвращать результат

# # # def get_sum(x, y): # x, y - параметры
# # #     result = x + y
# # #     return result

# # # print(get_sum(10, 20)) # 10, 20 - аргументы

# # # def comp_(laptop):
# # #     res = f' Ноутбук {laptop} починили'
# # #     return res

# # # message = comp_('hp')

# # # def send_mail(message):
# # #     print(f'Сообщение "{message}" доставлено!')

# # # send_mail(message)

# # # def pow_(a, b):
# # #     res = a ** b

# # # print(len('12121212'))

# # # def len_(a):
# # #     count = 0         
# # #     for i in a:
# # #         count = count + 1
# # #     return count # 4

# # # print(len_('asdasd'))

# # # from math import sqrt
# # # sqrt()

# # # def my_sqrt(num):
# # #     return num ** 0.5

# # # print(my_sqrt(25))

# # "Функции соблюдают принцип DRY (don't repeat yourself)"

# # '=======Аргументы и параметры====='

# # # параметры - переменные внутри функции, задаются при создании функции

# # # аргументы - значения, которые мы передаем при вызове функции

# # '==========Виды параметров========'
# # # 1. обязательные
# # # 2. не обязательные
# # #    1. с дефолтом(со значением по умолчанию)
# # #    2. args(все позиционные аргументы)
# # #    3. kwargs(все лишние именнованные аргументы)

# # # def func(*args, **kwargs):
# # #     print(*args)
# # #     print(kwargs)

# # # func(1,2,3,4,'hi', name = 'hi')

# # '===========Виды аргументов==========='
# # # 1. позиционные (по позиции)
# # # 2. именнованные (по названию (параметр = значение))


# # # def func(a,b,c,d):
# # #     ...
# # # func(d = 5, c = 3, a = 1, b = 0)


# # '----------------------------------------'
# # # num : int = 123
# # # name : str = 'makers'

# # # def sum_(a:int, b:int):
# # #     return a + b

# # # print(sum_(10, 3))

# # def calc_():
# #     try:
# #         num1 = float(input('Enter number: ')) 
# #         num2 = float(input('Enter number: '))  
# #         oper = input('Enter oper: ')  
# #         if oper == '+':
# #             print(num1+num2)
# #         elif oper == '-':
# #             print(num1-num2)
# #         elif oper == '/':
# #             print(num1/num2)
# #         elif oper == '*':
# #             print(num1*num2)
# #         elif oper == '**':
# #             print(num1**num2)
# #         else:
# #             raise KeyError
# #     except KeyError:
# #         print('вы ввели не ту операцию')
# #     except ValueError:
# #         print('введите число, а не символы')
# #     except ZeroDivisionError:
# #         print('нельзя делить на ноль')



# # calc_()



# db = [
#     {'name':'Tima', 'password':hash('123456789')},
#     {'name':'Nick', 'password':hash('205221000')}
# ]

# def in_database(name):
#     for user in db:
#         if name == user['name']:
#             return True
#     return False

# def register(name, password, password2):
#     if in_database(name):
#         raise Exception('Юзер с таким именем уже существует')
#     if password != password2:
#         raise Exception('Пароли не совпадают')
#     user = {'name':name, 'password':hash(password)}
#     db.append(user)
#     return 'Вы успешно зарегестрировались'

# def login(name, password):
#     if not in_database(name):
#         raise Exception('Пользователь не найден!')
#     for user in db:
#         if user['name'] == name:
#             if user['password'] != hash(password):
#                 raise Exception('Пароль не верный!')
            
#     return 'Вы успешно залогинились'

# print(register('katana', '123123123', '123123123'))
# print(db)
# print(login('katana', '12amsdbmnasdb'))

'============Lambda=============='
# lambda - анонимная функция, которая записывается в одну строчку

# def sum_1(y):
#     return y**2

# sum_1(10, 29)
# sum_1(1,5)
# sum_1(20,1)

# sum_2 = lambda y: y+y+y*y//y 


