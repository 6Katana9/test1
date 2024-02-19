'===============Циклы============'
# циклы - это блок кода, который отрабатывает несколько раз

"""Итерируемый обьект - это последовательность, которую мы можем перебрать. Например: 
[1,2,3] - list 
"hello world" - str
{"a":1, "b":2} - dict
(1,2,3,4,123,True) - tuple
"""
"""Итерация - процесс перебора итерируемого обьекта
"""
# 1. for - цикл, который работает с итерируемым обьектом, цикл заканчивает свою работу, когда он доходит до последнего элемента итерируемого обьекта

# 2. while - цикл, который работает до тех пор пока условие верное

'FOR'
# list_ = [1, True, 'hello', 0, 123]
# list_.remove(0)
# for elem in list_:
#     print(elem)


'WHILE'

# count = 100
# while count > 10: # True # Fasle
#     print(count)
#     count = count - 2

'=====Ключевые слова в циклах====='
# break - оператор, который останавливает работу цикла (ломает)
# continue - оператор, который пропускает итерацию (продолжает с другой итерации)

# range(start, end, step) - генератор последовательности, от start до end(не включительно)

# print(list(range(10, -1, -1)))

# for i in range(0, 21):
#     if i == 10:
#         continue
#     print(i)

# for i in ['1','2','3','world', '12']:
#     if i.isdigit():
#         print(int(i)) 
#         print('Все прошло хорошо!')
#     elif i.isalpha():
#         print('Я не могу перевести буквы в число')
#         break
#     else:
#         print('Я нашел символы!')


# count = 0
# passw = input('Введите пароль: ')
# while True:
#     print(count)
#     if str(count) == passw: 
#         print('Вот ваш пароль: ', passw)
#         break
#     count += 1  # count = count + 1

# count = 0
# while count < 3: 
#     break
#     print(count)
#     count += 1
# else: 
#     print('hi')

#else в цикле работает тогда когда условие цикла становится false, если же сработал break, то else не работает

