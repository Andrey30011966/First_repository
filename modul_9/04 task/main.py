first = 'Мама мыла раму'
second = 'Рамена мало было'

list_bool = list(map(lambda x, y: x == y, first, second))
print(list_bool)