import datetime
import multiprocessing

def read_info(name):
    all_data = []  # локальный список
    with open(name,'r') as file:
        while True:
            line = file.readline()              # пока считанная строка не окажется пустой
            all_data.append(line)               # добавляет каждую строку в список
            if not line:
                break



if __name__ == '__main__':                                                 # условие для выполнения процесса
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_line_time = datetime.datetime.now()                     # начало линейного подхода
    for x in filenames:
        read_info(x)
    finish_line_time = datetime.datetime.now()                    # конец  линейного подхода
    line_function_time = finish_line_time- start_line_time    # время выполнения линейного подхода
    print(f'Линейный вызов = {line_function_time}')



    start_multiprocessing = datetime.datetime.now()  # начало многопроцессного подхода
    with multiprocessing.Pool(processes=(len(filenames))) as pool:
        pool.map(read_info, filenames)              # метод map, многопроцессный подход
    finish_multiprocessing = datetime.datetime.now()                    # конец многопроцессного подхода
    multiprocessing_time = finish_multiprocessing - start_multiprocessing  # время многопроцессного подхода
    print(f'Многопроцессный  = {multiprocessing_time}')