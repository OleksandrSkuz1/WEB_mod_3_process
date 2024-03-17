from multiprocessing import Process, cpu_count
from multiprocessing.dummy import Pool
from threading import Thread
from time import time


def factorize_single(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize(*numbers):
    result = []
    for num in numbers:
        factors = factorize_single(num)
        result.append(factors)
    return result


def run_factorize(result, values):
    result.extend(factorize(*values))


def factorize_parallel(*numbers):
    result = []
    values = [numbers[i:i + 1] for i in range(len(numbers))]
    processes = []
    for value in values:
        proc = Process(target=run_factorize, args=(result, value))
        processes.append(proc)
        proc.start()
    for proc in processes:
        proc.join()
    return result


if __name__ == '__main__':
    # Синхронне виконання
    start_time = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end_time = time()
    print("Synchronous execution time:", round(end_time - start_time, 4), "seconds")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    # Паралельне виконання
    start_time = time()
    result = factorize_parallel(128, 255, 99999, 10651060)
    end_time = time()
    print("Parallel execution time:", round(end_time - start_time, 4), "seconds")
