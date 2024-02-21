'============JSON============='
#JavaScript Object Notation - универсальный формат, в котором мы можем храть данные в типах данных, понятных почти для всех языков программирования

# import json
# json_data = "null"
# python_data = json.loads(json_data)
# print(python_data)

# with open ('test.json', 'r') as file:
#     python_data = json.load(file)
# print(python_data)


# десериализация - перевод с json строки в python обьекты
# loads - метод для десериализации с json строки
# load - метод для десериализации с json файла

import json
# python_data = None
# json_data = json.dumps(python_data)
# print(json_data)


python_data = [1, 2, True, False, None, 'makers']
with open ('test.json', 'w') as file:
    json.dump(python_data, file)


# сериализация - перевод python обьектов в json строку
# dumps - метод для сериализации в json строку
# dump - метод для сериализации в json файл

