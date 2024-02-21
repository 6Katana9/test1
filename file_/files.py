'=========Module & package======'
# .py - module
# more modules - package

'=============File============'
#open() - функция, которая открывает файл в определенном режиме

# r - read (только для чтения)
# w - write (только для записи, каждый раз файл очищается)
# a - append (только для дозаписи, добавляется в конец)
# x - создает файл, но если он существует выйдет ошибка

'==============Read============='
# file = open('test1.txt', 'r')
# print(dir(file))
# print(file.writable()) # False
# print(file.readable()) # True
# print(file.read()) # read file
# file.seek(0)
# print(file.read())
# print(file.read(10))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.tell())
# print(file.readline())
# print(file.tell())

# file.close()
'read:str, readline:str, readlines:List[str]'

''

'=============Write=============='
# file = open('test1.txt','w') 
# file.write('Makers HELLO WORLD')
# file.writelines(['hello world\n', 'makers\n'])
# file.close()

'write(str), writelines(List[str,str])'

'=============Append============='
#  добавляет записи в конец

# file = open('test1.txt', '')
# file.write('py33\n')
# file.seek(0)
# file.write('py32\n')
# file.close()

'========Контекстный менеджер====='
# with

with open('test1.txt', '') as file:
    print(file.read())

print(file.closed) # True - файл закрылся


