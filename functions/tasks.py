# data_ = FormatData(data)
# prepared_data = data_.prepare()

# writer = FileWriter('data.txt')
# writer.write_file(prepared_data)
            
# 2 O -> Open-Closed Principle (OCP) 
# Принцип открытости/закрытости (открыт для расширения, закрыт для изменения (модификации))

# class Discount:
#     def init(self, customer, price):
#         self.customer = customer 
#         self.price = price

#     def give_discount(self):
#         if self.customer == 'fav':
#             return self.price * 0.05
#         if  self.customer == 'vip':
#             return self.price * 0.2

'''соблидение принципа OCP''' 

# class Discount:
#     def init(self, customer, price):
#         self.customer = customer 
#         self.price = price

#     def give_discount(self):
#         return self.price * 0.05


# class VIPDiscount(Discount):
#     def give_discount(self):
#         return super().give_discount() * 0.2


# class VIPSDiscount(Discount):
#     def give_discount(self):
#         return super().give_discount() * 0.4
    

# 3. Liskov Substitution Principle
# Принцип постановки Лисков
# Для любого класса клиент должен иметь возможность использовать любой подкласс (Дочерний), не замечая разницы между ними (поведение программы не должно меняться)

# class Animal:
#     def init(self, attrs):
#         self.attrs = attrs

#     def eat(self):
#         print('ate some food')

# class Cat(Animal):
#     def eat(self, amount=0.1):
#         if amount > 0.3:
#             print('Слишком много')
#         else:
#             print('ate some food')

# class Dog(Animal):
#     def eat(self):
#         print('Ate some doog\'s food')


# pluto = Dog({'name': 'Pluto', 'age': 3})
# bethoven = Dog({'name': 'Bethove', 'age': 2})
# cat =  Cat(('Garfild', '4'))


# animals = [pluto, bethoven, cat]
# for animal in animals:
#     if animal.attrs['age'] > 2:
#         print('Взрослое животное')


# class Animal:
#     def init(self, name, age):
#         self.attrs = {'name': name, 'age': age}

#     def eat(self, amount=0):
#         print('ate some food')

# class Cat(Animal):
#     # def init(self, name, age):
#     #     super().init(name, age)

#     def eat(self, amount=0.1):
#         if amount > 0.3:
#             print('Слишком много')
#         else:
#             print('ate some food')

# class Dog(Animal):
#     # def init(self, name, age):
#     #     super().init(name, age)

#     def eat(self, amount=0):
#         print('Ate some doog\'s food')

# pluto = Dog('pluto', 3)
# bethoven = Dog('Bethove',2)
# cat =  Cat('Garfild', 4)

# animals = [pluto, bethoven, cat]

# for animal in animals:
#     if animal.attrs['age'] > 2:
#         print('Взрослое животное')
#     animal.eat(9)
        

# 4. I -> Interface Segregation Principle
# Принцип разделения интерфейсов

# class Shape:
#     def draw(self):
#         raise NotImplementedError('Нужно переопределить')
    
# class Circle(Shape):
#     def draw(self):
#         pass

# class Rectangle(Shape):
#     def draw(self):
#         pass


        
# class Creature:
#     def init(self, name):
#         self.name = name

#     def swim(self):
#         pass

#     def fly(self):
#         pass

#     def walk(self):
#         pass

#     def talk(self):
#         pass

# class Human(Creature):
#     pass

# class Fish(Creature):
#     pass


# правильно
          
# class Creature:
#     def init(self, name):
#         self.name = name

# class Swimmer:
#     def swim(self):
#         pass

# class Walker:
#     def walk(self):
#         pass

# class Talker:
#     def talk(self):
#         pass

# class Flyer:
#     def fly(self):
#         pass


# class Human(Creature, Walker, Talker, Swimmer):
#     ...

# class Fish(Creature, Swimmer, Flyer):
#     pass

# class Bird(Creature, Walker, Flyer, Swimmer):
#     ...

# 5. D -> Dependency Inversion Principle
#  Принцип инверсии зависимостей
        


# class TerminalWriter:
#     def write(self, msg):
#         print(msg)

Aiana, [15/2/24 17:23]
# class FileWriter:
#     def write(self, msg):
#         with open('log.txt', 'w') as file:
#             file.write(msg)

# import time

# class Logger:
#     def init(self):
#         self.prefix = time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())

#     def log_str(self, msg):
#         TerminalWriter().write(msg)

#     def log_file(self, msg):
#         FileWriter().write(msg)


# logger = Logger()
# print(logger.prefix)
# logger.log_str('hello')
        

'''========='''
# class TerminalWriter:
#     def write(self, msg):
#         print(msg)

# class FileWriter:
#     def write(self, msg):
#         with open('log.txt', 'w') as file:
#             file.write(msg)


# class TestWriter:
#     pass


# import time

# class Logger:
#     def init(self):
#         self.prefix = time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())


#     def log(self, message, logger):
#         logger().write(message)
    
# l = Logger()
# l.log('hello', FileWriter)
    
# l2 = Logger()
# l2.log('test', TerminalWriter)
# l3= Logger()
# l3.log('hhh', TestWriter)

Aiana, [15/2/24 17:26]
# SOLID

# SOLID — это аббревиатура для набора принципов проектирования, созданных для разработки программного обеспечения при помощи объектно-ориентированных языков. Принципы SOLID направленны на содействие разработки более простого, надежного и обновляемого кода.

# При правильной реализации это делает ваш код более расширяемым, логичным и легким для чтения.

# region S (SRP)
# 1. Single Responsibility Principle
# (Принцип единственной обязанности)
# Принцип единственной обязанности требует того, чтобы один класс выполнял только одну работу. (Т.е не надо создавать огромный класс который делает все)

# before
# class ExportCsv:
#     def init(self, raw_data):
#       self.data = self.prepare(raw_data)


#     def prepare(self, raw_data):
#       result = ''
#       for item in raw_data:
#           new_line =  f"{item['name']}, {item['surname']}\n"
#           result += new_line
#       return result

        
#     def write_file(self, filename):
#       with open(filename, 'w') as f:
#           f.write(self.data)


# data = [
#   {
#     'name': 'Sherlock',
#     'surname': 'Holmes',
#   },
#   {
#     'name': 'John',
#     'surname': 'Watson',
#   }
# ]

# exporter = ExportCsv(data)
# exporter.write_file('out.csv')

# after

# class FormatData:
#     def init(self, raw_data):
#         self.raw_data = raw_data

    
#     def prepare(self):
#         result = ''
#         for item in self.raw_data:
#             new_line =  f"{item['name']}, {item['surname']}\n"
#             result += new_line
#         return result


# class FileWriter:
#     def init(self, filename):
#         self.filename = filename


#     def write(self, data):
#         with open(self.filename, 'w') as f:
#             f.write(data)


# data = [
#   {
#     'name': 'Sherlock',
#     'surname': 'Holmes'
#   },
#   {
#     'name': 'John',
#     'surname': 'Watson'
#   }
# ]

# formatter = FormatData(data)
# formatted_data = formatter.prepare()

# writer = FileWriter('out.csv')
# writer.write(formatted_data)


# Рассмотрим объект "Выпивоха" (Tippler).
# Для выполнения принципа SRP разделим обязанности на троих:


# Один наливает (PourOperation)
# Один выпивает (DrinkUpOperation)
# Один закусывает (TakeBiteOperation)

# плюсы:

# Код стал предельно ясен на каждом уровне
# Код могут писать несколько программистов сразу (каждый пишет отдельный элемент)
# Упрощается автоматическое тестирование — чем проще элемент, тем легче его тестировать
# Из этих трех операций, в будущем, вы сможете сложить обжору ( используя только TakeBitOperation), Алкоголика (используя только DrinkUpOperation напрямую из бутылки) и удовлетворить многие другие требования бизнеса.

# минусы:
# Придется создать больше типов.
# Выпивоха впервые выпьет на пару часов позже, чем мог бы


# endregion

# region O (OCP)

# 2. Open-Closed Principle
# (Принцип открытости/закрытости)

# Программные сущности (классы, модули, функции) должно быть открыты для расширения, но не модификации.



# class Discount:
#   def init(self, customer, price):
#       self.customer = customer
#       self.price = price
#   def give_discount(self): # скидку для обычных покупателей одну для других другую если еще заходим добавить еще прийдется писать
#       if self.customer == 'fav':
#           return self.price * 0.2
#       if self.customer == 'vip':
          # return self.price * 0.4

# Чтобы следовать OCP, мы добавим новый класс, который будет расширять Discount. И в этом новом классе реализуем требуемую логику:

# class Discount:
#     def init(self, customer, price):
#       self.customer = customer
#       self.price = price
#     def get_discount(self):
#       return self.price * 0.2

# class VIPDiscount(Discount):
#     def get_discount(self):
#       return super().get_discount() * 2
# # Если вы решите дать скидку супер VIP пользователям, то это будет выглядеть так:
# class SuperVIPDiscount(VIPDiscount):
#     def get_discount(self):
#       return super().get_discount() * 4
# Расширяйте, но не модифицируйте.

# before
# import sys
# import time

Aiana, [15/2/24 17:26]
# class Logger:
#     def log(self, message):
#         current_time = time.localtime()
#         sys.stderr.write(f"{time.strftime('%Y-%b-%d %H:%M:%S', current_time)} --> {message}\n")


# logger = Logger()
# logger.log('An error has happened!')


# after

# import sys
# import time


# class Logger:
#     def init(self):
#         self.format = '%Y-%b-%d %H:%M:%S -->'
        
#     def log(self, message):
#         prefix = time.strftime(self.format, time.localtime())
#         sys.stderr.write(f"{prefix} {message}\n")


# class CustomerLogger(Logger):
#     def init(self):
#         super().init()
#         self.format = '%Y-%b-%d ::'


# logger = Logger()
# logger.log('An error has happened!')

# c_logger = CustomerLogger()
# c_logger.log('Custom logged message!')


# endregion

# region L (LSP)
# 3. Liskov Substitution Principle
# (Принцип подстановки Лисков)

# Главная идея, стоящая за Liskov Substitution Principle в том, что для любого класса клиент должен иметь возможность использовать любой подкласс базового класса, не замечая разницы между ними, и следовательно, без каких-либо изменений поведения программы при выполнении. Это означает, что клиент полностью изолирован и не подозревает об изменениях в иерархии классов.

# LSP это основа хорошего объектно-ориентированного проектирования программного обеспечения, потому что он следует одному из базовых принципов ООП — полиморфизму. Речь о том, чтобы создавать правильные иерархии, такие, что классы, производные от базового являлись полиморфными для их родителя по отношению к методам их интерфейсов.

# Если по простому - родительский класс можно заменить на дочерний не ломая логику работы программы. Т.е наследование должно быть логичным что если в родители и потомке есть какой то метод этот метод должен принимать одинакове количество аргументов, примерно одной и той же логике следовать

# before

# class Animal:
#     def init(self, attrs):
#         self.attributes = attrs
    

#     def eat(self): # методы отличаются у всех классов
#         print("Ate some food!")


# class Cat(Animal):
#     def eat(self, amount = 0.1):
#         if amount > 0.3:
#             print("Can't eat that much!")
#         else:
#             print("Ate some cat food!")
    

# class Dog(Animal):
#     def eat(self):
#         print("Ate some dog food!")


# pluto = Dog({'name': 'Pluto', 'age': 3}) # 1) точно не понятно как передавать аргументы классу 
# goofy = Dog({'name': 'Goofy', 'age': 2})
# buttons = Cat(('Mr. Buttons', 4))

# animals = (pluto, goofy, buttons)

# for animal in animals: # из за 1) не будет это работать
#     if animal.attributes['age'] > 2:
#         print(animal.attributes['name'])

# endregion

# region I (ISP)

# 4. Interface Segregation Principle
# (Принцип разделения интерфейсов)

# Создавайте тонкие интерфейсы, которые ориентированы на клиента. Клиенты не должны зависеть от интерфейсов(или же методов которые не использует), которые они не используют. Этот принцип устраняет недостатки реализации больших интерфейсов.

# class IShape:
#     def draw(self):
#         raise NotImplementedError # Исключение, возникающее в случаях, когда наследник класса не переопределил метод, который должен был


# class Circle(IShape):
#     def draw(self):
#         pass

# class Square(IShape):
#     def draw(self):
#         pass

# class Rectangle(IShape):
#     def draw(self):
#         pass
# a = Circle()
# a.draw()

# Хороший пример:

# class Creature:
#     def init(self, name):
#         self.name = name
#     def swim(self):
#         pass
#     def walk(self):
#         pass
#     def talk(self):
#         pass
       

# class Human(Creature):
#     def init(self, name):
#         super().init(name)
#     def swim(self):
#         print(f"I'm {self.name} and I can swim") 
#     def walk(self):
#         print(f"I'm {self.name} and I can walk") 
#     def talk(self):
#         print(f"I'm {self.name} and I can talk")

# class Fish(Creature):
#     def init(self, name):
#         super().init(name)
#     def swim(self):
#         print(f"I'm {self.name} and I can swim") 
# class Cat(Creature):
#     def init(self, name):
#         super().init(name)
#     def swim(self):
#         print(f"I'm {self.name} and I can swim")
#     def walk(self):
#         print(f"I'm {self.name} and I can walk")


# human = Human("John Doe")
# human.swim()
# human.walk()
# human.talk()

# fish = Fish("Nemo")
# fish.swim()

# cat = Cat("Mr. Buttons")
# cat.walk()
# cat.swim()
# cat.talk() # кошкак не умеет говорить!

# теберь можно подключать только нужные интерфейсы

# class Creature:
#     def init(self, name):
#         self.name = name


# class SwimmerInterface:
#     def swim(self):
#         pass


# class WalkerInterface:
#     def walk(self):
#         pass


# class TalkerInterface:
#     def talk(self):
#         pass
       

# class Human(Creature, SwimmerInterface, WalkerInterface, TalkerInterface):
#     def init(self, name):
#         super().init(name)


#     def swim(self):
#         print(f"I'm {self.name} and I can swim")


#     def walk(self):
#         print(f"I'm {self.name} and I can walk") 


#     def talk(self):
#         print(f"I'm {self.name} and I can talk") 


# class Fish(Creature, SwimmerInterface):
#     def init(self, name):
#         super().init(name)


#     def swim(self):
#         print(f"I'm {self.name} and I can swim") 


# class Cat(Creature, SwimmerInterface, WalkerInterface):
#     def init(self, name):
#         super().init(name)


#     def swim(self):
#         print(f"I'm {self.name} and I can swim")


#     def walk(self):
#         print(f"I'm {self.name} and I can walk")


# human = Human("John Doe")
# human.swim()
# human.walk()
# human.talk()

# fish = Fish("Nemo")
# fish.swim()

# cat = Cat("Mr. Buttons")
# cat.walk()
# cat.swim()



# endregion

# region D (DIP)

# 5. Dependecy Inversion Principle
# (Принцип инверсии зависимостей)

# Зависимость должна быть от абстракций, а не от конкретики. Модули верхних уровней не должны зависеть от модулей нижних уровней. Классы и верхних, и нижних уровней должны зависеть от одних и тех же абстракций. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций


# befor

# import sys
# import time


# class TerminalPrinter: # norm
#     def write(self, msg):
#         sys.stderr.write(f"{msg}\n")


# class FilePrinter: # norm
#     def write(self, msg):
#         with open('log.txt', 'a+', encoding='UTF8') as f:
#             f.write(f"{msg}\n")


# class Logger: # зависит от двух других классов
#     def init(self):
#         self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime()) # можно опять применить OCP


#     def log_stderr(self, message): #  вызывает write для конкретно класс
#         TerminalPrinter().write(f"{self.prefix} {message}")


#     def log_file(self, message): # Тут тоже
#         FilePrinter().write(f"{self.prefix} {message}")


# logger = Logger()
# logger.log_file("Starting the program...")
# logger.log_stderr("An error!")

# # after

# import sys
# import time


# class TerminalPrinter:
#     def write(self, msg):
#         sys.stderr.write(f"{msg}\n")


# class FilePrinter:
#     def write(self, msg):
#         with open('log.txt', 'a+', encoding='UTF8') as f:
#             f.write(f"{msg}\n")


# class Logger:
#     def init(self):
#         self.format = '%Y-%b-%d %H:%M:%S' # теперь формат можно менять


#     def log(self, message, notifier):
#         prefix = time.strftime(self.format, time.localtime())
#         notifier().write(f"{prefix} {message}")


# logger = Logger()
# logger.log("Starting the program...", TerminalPrinter)
# logger.log("An error!", FilePrinter)

# endregion