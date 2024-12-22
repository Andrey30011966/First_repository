# from pprint import pprint
import pandas as pd
import numpy as np
# import requests

"""В этих примерах мы отправляем GET, POST и PUT-запросы к различным URL 
    и выводим код состояния ответа, заголовки и тело ответа."""
#
# response = requests.get('https://api.github.com/events')
# print(response.status_code)
# print(response.headers)
# pprint(response.json())
#
# data = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://httpbin.org/post', data=data)
# print(response.status_code)
# pprint(response.json())
#
# data = {'key1': 'value1', 'key2': 'value2'}
# response = requests.put('https://httpbin.org/put', data=data)
# print(response.status_code)
# pprint(response.json())

"""Примеры использования pandas"""

# data = {
#     'Имя': ['Анна', 'Борис', 'Вера'],
#     'Возраст': [28, 34, 29],
#     'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск']
# }
#
# df = pd.DataFrame(data)
# print(df)
#
# # Чтение данных из CSV файла
# # df = pd.read_csv('data.csv')
#
# # Чтение данных из Excel файла
# # df = pd.read_excel('data.xlsx')
#
# # Получение всех записей, где возраст больше 30
# filtered_df = df[df['Возраст'] > 30]
# print(filtered_df)

"""Примеры использования NumPy"""

# Создание одномерного массива
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Создание двумерного массива (матрицы)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)

# Синус всех элементов массива
angles = np.array([0, np.pi/2, np.pi])
sin_values = np.sin(angles)
print(sin_values)

# Экспоненциальная функция
a = np.array([0, 1, 2])
exp_values = np.exp(a)
print(exp_values)