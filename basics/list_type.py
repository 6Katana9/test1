'=============List=============='
# списки - изменяемый, индексируемый, упорядоченный, итерируемый тип данных, предназначенный для храения любых данных в определенном порядке

list1 = [34, 5,[1,4,20, [3,2,0]], 0, 'makers', 'num', [1,2,3],12]
# print(list1[3:-2])
# print(list1[-1])
# print(list1[5][2])
# print(list1[2][3][2])

string = 'hello'
res = list(string)
# print(res) # ['h','e','l','l','o']

# list_ = []
# list_ = list()
# list_ = [2] * 10
# print(list_)

'===========Методы списков==============='
# append - добавление элементы в конец списка
# list_ = []
# list_.append(True)
# list_.append('text')
# list_.append(123)
# list_.append([1,2,3])
# print(list_) # [True, 'text', 123, [1,2,3]]

# pop - удаляет элемент из списка по индексу и возвращает удаленный элемент, если не передать индекс в скобки то удаляет последний элемент

# list_ = [51,'hi', True, 123,'q', 12, 0]
# rm_elem = list_.pop(3)
# print(rm_elem) # 123
# print(list_) # [51,'hi', True,'q', 12, 0]

'------------------------------------'
# remove - удаление элемента из списка по значению

# list_ = [12, 'makers',234, 0, False, 1, 1, 1]
# list_.remove('makers')
# print(list_) 

'---------------------------------------'
# count - метод, который считает кол-во элементов в списке

# list_ = [0, 12, 'hi', True, False, True, 0, 1, 1, 0]
# count_of_elem = list_.count(1)
# print(count_of_elem)  # 4

'-----------------------------'
#index - возвращает индекс первого вхождения указанного элемента

list_ = [12, 1, 1, 1, 'hi', None]
index_ = list_.index('hi')
print(index_) # 4

'---------------------------------'
#insert - добавляет элемент в список по указанному индексу

# list_ = [87,11,23,'hi',5,1,True,'world']
# list_.insert(7, False)
# print(list_)
'------------------------------'
#extend - добавляет элементы списка в другой список
# list1 = [0,0,0]
# list2 = ['hi', True, None, 123, 12]
# list1.extend(list2) # [0,0,0, 1,2,3 ]
# print(list1)
'-------------------------'

#reverse - расставляет элементы в обратном порядке
# list_ = [1,2,3,4, None, [1,2,3]]
# list_.reverse()
# print(list_) # [[1,2,3], None, 4, 3, 2, 1]

#sort - сортирует список, состоящий из элементов одного типа данных
# list_ = [23, 1, 24, 23, 123, 0]
# list_.sort()
# print(list_) # [0, 1, 23, 23, 24, 123]

list_ = ['makers', 'hi', 'asd' ,'qwerty']
list_.sort(key=len, reverse=True)
# print(list_) # ['makers', 'qwerty', 'asd', 'hi']

'==================Tuple================'
# кортеж - упорядоченный, неизменяемый, итерируемый тип данных, литералы (,)

tuple_ = (1,2,3,True, False, None, 'hi')
# print(dir(tuple()))

# есть только 2 метода это - index и count

# a = 12, 5, 'hi'
# print(a)

list_ = [1,2,34,'hi',True, None]
# print(list_[0])
# print(list_[1])
# print(list_[2])
# print(list_[3])
# print(list_[4])
# print(list_[5])

'aksdjaskldjaskjd KAKLASKJDL 12JA'

for i in list_: 
    print(i) 