'=============Словари============='
# dict - изменяемый, итерируемый, неупорядоченный, неиндексируемый тип данных, для хранения данных в парах(ключ:значение) 

# user = {'a':{1:'a', 2:'b'}, 'a':20, 'c':20}

# print(user)
# print(user['a']) # 123
# print(user['c']) # 20
# print(user['b']) # 20

# {ключ:значение, ключ:значение...}
#ключ - неизменяемый тип данных, уникальный(если ключ повторяется, то сохранится тот, который является последним)
#значение - любые: и изменяемый, и неизменяемый тип данных. Могут повторяться

'===============Создание=========='
# dict1 = {'a':1,'b':2}
# dict2 = dict([('a',1),('b',2)])
# dict3 = dict(['a1','b2'])

dict4 = {}
dict4['name'] = 'tima'
dict4['age'] = 100
dict4['nick'] = 'collection'
print(dict4)

'=========Методы словарей========='
# get - метод, который возвращает значение по ключу, если такого члюча нет то возвращает дефолтное значение, чаще всего None
# user = {
#     'name':'Nick',
#     'age': 100,
#     'telephon_number':'+1234567'
# }
# print(user['asfasda']) # KeyError
# print(user.get('age123', 'Нет такого ключа')) # 100
# print(user.get('name')) # Nick
# print(user.get('id')) # None

#pop - удаляет пару по ключу и возвращает значение
# dict_ = {'a':1, 'b':2, 'c':3}
# popped_values = dict_.pop('a')
# print(popped_values) # 1
# print(dict_) # {'b':2, 'c':3}

#popitem - удаляет последнюю пару и возвращает ее
# dict_ = {'a':1, 'b':2, 'c':3}
# popped_values = dict_.popitem()
# print(popped_values) # ('c', 3)

# print(dir(dict()))

# update - расширяет словарь парами из второго словаря

# dict1 = {1:'a',2:'b'}
# dict2 = {2:'c',4:'d'}
# dict1.update(dict2)
# print(dict1) # {1:'a', 2:'c', 4:'d'}

# clear - очищает словарь
# dict_ = {1:1, 2:2, 3:3}
# dict_.clear()
# print(dict_) # {}

# fromkeys - метод для создания нового словаря, используя список ключей

# dict_ = dict.fromkeys([1,2])
# print(dict_) #{1: None, 2: None}

# dict2 = dict.fromkeys('abcd', 0)
# print(dict2) # {'a':0, 'b':0, 'c':0, 'd':0}

# list.copy(), list.deepcopy()
# dict.setdefault()

# items - метод, который достает [(ключ, значение),(ключ, значение)...]
# keys - метод, который возвращает ключи
# values - метод, который возвращает значения

# dict_ = {'a':1, 'b':2, 'c':3}
# print(dict_.values())
# print(dict_.keys())
# print(dict_.items())

'=========Циклы с dict=========='
dict_ = {'a':1, 'b':2, 'c':3}

for k, v in dict_.items():
    print(f'ключ - {k}, а значение - {v}')

'''
У вас есть словарь:
dict_ = {'a':1, 'b':2, 'c':3}

Вам нужно поменять ключи и значения местами, чтобы получилось вот так:

dict_2 = {1:'a',2:'b',3:'c'}
'''
# dict_ = {'a':1, 'b':2, 'c':3}
dict_2 = {}
for a, b in dict_.items():
    dict_2[b] = a
print(dict_2)

dict().setdefault()
list().copy()
list().deepcopy()