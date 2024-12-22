from threading import Thread
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()
for word_count, file_name in [(10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt')]:
    thread = Thread(target=write_words, args=(word_count, file_name))
    thread.start()
    thread.join()
end_time = time.time()

print(f'Работа потока {time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))}')

start_time1 = time.time()
for word_count, file_name in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    write_words(word_count, file_name)
end_time1 = time.time()

print(f'Работа потока {time.strftime("%H:%M:%S", time.gmtime(end_time1 - start_time1))}')