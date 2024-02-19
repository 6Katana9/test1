'===========Встроенные функции========='
# map, filter, reduce, zip, enumerate


'ZIP'
# соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple) (zip object)

# list_1 = [1, 2, 3, 4]
# list_2 = ['a', 'b', 'c']
# list_3 = [10.5, 20.0, 1.3, 0.5]

# zipped = zip(list_1, list_2, list_3)
# print(zipped) # <zip object at 0x7f8ajs23fs>
# # print(list(zipped)) # [(1, 'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3)]
# # print(tuple(zipped)) # ((1, 'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3))
# print(dict(zipped)) # будет работать только с двумя листами в zip()
 
'ENUMERATE'
# нумерует последовательность (по дефолту с 0), (тоже возвращает генератор ) 
# <enumerate object 0x7kjf8392sjd90>

# enumerated = enumerate([True, 1, 'hi', 2193, None, False], 100)
# print(enumerated) #<enumerate object 0x7kjf8392sjd90>
# # print(list(enumerated)) #[(0, 'h'), (1,'e'),(2, 'l')....]
# for elem in enumerated:
#     print(elem)

'MAP'
# принимает функцию и последовательность
# записывает в новую последовательность результат функции, приминив ее на каждый элемент последовательности
# <map object 0x7djsf9jidf9qj>
# int('23') # 23
# list_ = ['1', '23', '3', '4']
# mapped = map(int, list_) # <map object 0x7djsf9jidf9qj>
# print(list(mapped))  # [1, 23, 3, 4]

# # mapped2 = map(str.isdigit, list_) # [False, True, False, False]
# print(list(mapped2))

list_ = [12, 34, 1, 2, 6]

def pow_(x,y):
    return x ** y

print(list(map(pow_, list_)))

# print(list(map(lambda x:x**2, list_)))

# str_ = 'hello world'
# mapped = map(str.upper, str_)
# print(''.join(list(mapped)))

# print(''.join(list(map(str.upper, 'hello world'))))

'FILTER'
# возвращает генератор с элементами, прошедшими фильтрацию (какое-то условие), принимает функцию и последовательность
# <filter object 0x7jdfj9292k29>

# list_ = [12, -23, 0, -1, -34, 38]
# filtered = filter(lambda x: x >= 0, list_)
# print(list(filtered))

# users = [
#     {'name':'makers', 'age':20},
#     {'name':'anonym', 'age':15},
#     {'name':'sem', 'age':25}
# ]
# # оставить тех юзеров у которых возраст больше 18

# [{'name':'makers', 'age':20},{'name':'sem', 'age':25}]

# filtered = filter(lambda x: x['name'].startswith('A'), users)
# print(list(filtered))

'REDUCE'
# принимает функцию и последовательность, возвращает 1 элемент (передаваемая функция должна принимать 2 аргумента)
# импортируется из functools

# from functools import reduce

# list_ = ['1','2','3','1','5','10']
# res = reduce(lambda x, y: x + y, list_)
# print(res)

# '1231510'
# 300
# 

# users = [
#     {'name':'makers', 'age':20},
#     {'name':'anonym', 'age':15},
#     {'name':'sem', 'age':25}
# ]
# выведите самого младшего юзера используя reduce
# {'name':'anonym', 'age':15}
# from functools import reduce

# def func(x, y):
#     if x['age'] < y['age']:
#         return x
# #     else:
# #         return y
    
# # print(reduce(func, users))

# from functools import reduce
# list_ = [1,2,4,6,1,9,-1,6,-12]
# # выведите самое маленькое число, с помощью reduce
# res = reduce(lambda x, y: x if x<y else y, list_)
# print(res)

# def func(x,y):
#     if x < y:
#         return x
#     else: 
#         return y
    
# res = reduce(func, list_)
# print(res)