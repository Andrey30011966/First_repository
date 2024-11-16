import time
from datetime import timedelta
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./example{number}.txt' for number in range(1, 5)]

start_time = time.time()

for filename in filenames:
    read_info(filename)

end_time = time.time()

duration = timedelta(seconds=end_time - start_time)
print(f'Линейное выполнение: {duration}')



def multiprocess_read_file(name):
    start_time = time.time()

    with Pool() as pool:
        pool.map(read_info, filenames)

    end_time = time.time()

    duration = timedelta(seconds=end_time - start_time)
    print(f'Многопроцессное выполнение: {duration}')

if __name__ == '__main__':
    filenames = [f'./example{number}.txt' for number in range(1, 5)]
    multiprocess_read_file(filenames)