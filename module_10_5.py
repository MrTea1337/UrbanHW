from datetime import datetime
from multiprocessing import Pool

start_time = datetime.now()


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line != '':
            all_data.append(line)
            line = file.readline()


#  Линейный вызов
# filenames = [f'./file {number}.txt' for number in range(1, 5)]
# for name in filenames:
#     read_info(name)
# end_time = datetime.now()
# print(end_time - start_time)

# Многопроцессный
if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = datetime.now()
    print(end_time - start_time)
