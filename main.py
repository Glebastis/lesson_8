import time
import os
import random
import psutil



def show_information(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        print('Исп. память до вып. функции:' + str(proc.memory_info().rss / 1000000))
        start = time.time()
        f(*args, **kwargs)
        print('Исп. память после вып. функции:' + str(proc.memory_info().rss / 1000000))
        stop = time.time()
        print("Заняло {} секунд".format(stop-start))
    return wrapper

@show_information
def generator_example_1(num):
    for i in range(num):
        yield(i)

@show_information
def list_example_1(num):
    temp_list = []
    for i in range(num):
        temp_list.append(i)
    return(i)

generator_example_1(1000000)

list_example_1(1000000)