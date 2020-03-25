from threading import Thread
import time
from time import ctime
from time import perf_counter


def func1():

    print(ctime())

    print('Working1')
    time.sleep(7)

    print('Working1 completed')
    print(ctime())
    end = perf_counter()
    print(end - start)


def func2():
    print('Working2')
    time.sleep(5)
    print('Working2 completed')


def func3():
    print('Working3')
    time.sleep(3)
    print('Working3 completed')


def func4():
    print('Working4')
    time.sleep(1)
    print('Working4 completed')


if __name__ == '__main__':
    start = perf_counter()
    Thread(target=func1).start()
    Thread(target=func2).start()
    Thread(target=func3).start()
    Thread(target=func4).start()
