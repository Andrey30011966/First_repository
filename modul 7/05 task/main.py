import os
import time

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime('%d-%m-%y %H:%M:%S', time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file},\nПуть: {filepath},\nРазмер: {filesize} байт,\nВремя изменения: {formatted_time},\n'
            f'Родительская директория: {parent_dir}\n')