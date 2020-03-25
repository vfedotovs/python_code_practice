from threading import Thread
import time
from time import ctime
from time import perf_counter


def func1():
    #t = time()
    print(ctime())
    print('Working1')
    time.sleep(7)
    print('Working1 completed')


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
    #t = time()
    print(ctime())


if __name__ == '__main__':
    start = perf_counter()
    func1()
    func2()
    func3()
    func4()
    end = perf_counter()
    print(end - start)
