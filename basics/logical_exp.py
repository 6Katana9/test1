# '=Логические и условные операторы='
# # Логические операторы - выражения, которые возвращают True, если выражение верное, False - если выражение не верное

# 'равенство'
# 5 == 6 # False
# 5 == 5 # True

# 'не равенство'
# 4 != 5 # True
# 5 != 5 # False

# 'больше'
# 10 > 0 # True
# -5 > 2 # False

# 'меньше'
# 5 < 4 # False
# 5 < 10 # True

# 'больше или равно'
# 5 >= 10 # False
# 10 >= 5 # True
# 5 >= 5 # True

# 'меньше или равно'
# 10 <= 5 # False
# 5 <= 10 # True
# 5 <= 5 # True

# # a = 10
# # b = '10'
# # print(a == b) # True

# # a = 'd'
# # b = 'i'

# # print(a < b) # True

# '========And, Or, Not==========='
# # and - и
# # or - или
# # not - не

# 'AND'
# a = 5
# b = 6

# # True  и  True --> True
# a == 5 and b == 6  
# # True  и  False --> False
# a == 5 and b == 3
# # False и  False --> False
# a > 10 and b < 2

# # возвратится True, если с права True И слева True. 
# # если хотябы с одной стороны будет False, либо сразу в двух сторонах то возвратится False

# 'OR'
# a = 20
# b = 5

# #True  или True --> True
# a == 20 or b > 1
# #True  или False --> True
# a == 20 or b < 1
# #False или True --> True
# a > 100 or b == 5 
# #Fasle или False --> False
# a < 10 or b < 1

# # если хотябы одна часть выражения True, то будет True

# 'NOT'

# # not False - True
# # not True - False
# a = 5
# not a < 10 # False
# not a != 5 # True

# not not not not not a != 10 # True

# b = 10
# c = 5
# print(not b <= 10 or c > 10)


'==========Boolean Type==========='
# Булевый тип данных имеет всего 2 значения

# Булевый тип данных используется в условных операторах, для выполнения ситуативных задач

bool(1) # True
bool(0) # False
bool(-123) # True

bool('hello') # True
bool(' ') # True
bool('') # False

bool(True) # True
bool(False) # False

bool([]) # False
bool([[]]) # True

'==========None Type==========='
# None - неизменяемый тип данных с одним значением - None, который используется для обозначения отсуствия значения

a = None
print(a)

bool(None) # False
bool('None') # True

'=========Условные операторы======'
# условные операторы - конструкция, которая используется для того, чтобы при разных входных данных код работал по разному



# pogoda = 'dojd`'

# if pogoda == 'dojd`':
#    print('Взял зонт')
# elif pogoda == 'sneg':
#    print('Взял куртку')
# elif pogoda == 'solnce':
#    print('Взял очки')
# else:
#    print('Остался дома')

# '------------'
# if условие 1:
#     тело1
# '------------'
# if условие1:
#     тело1 # тело1 будет выполняться если условие1-True
# else:
#     тело2 # тело2 будет работать во всех других случаях
# '------------'
# if условие1:
#     тело1
# elif условие2:
#     тело2
# '-----------'
# if условие1:
#     тело1
# elif условие2:
#     тело2
# else:
#     тело3

# num = int(input('Введите число: '))
# if num < 0:
#     print(f'Число {num}-положительное')
'-----------------------'
# if num < 0:
#     print(f'Число {num}-положительное')
#     if 
# else:
#     print('If не сработал, elif не сработал')


# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# oper = input('Введите оператор: ')


# 10 / 0

'Тернарный оператор'
# тернарный оператор - условие в одну строку

# telo1 if uslovie1 else telo2

# a = -20
# res = a ** 2 if a > 0 else a - 2
# print(res)

# a = -20 
# if a > 0:
#     res = a ** 2
# else:
#     res = a - 2
# print(res) # -22