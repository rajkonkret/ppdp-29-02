import time
import numpy as np  # np to alias


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Czas wykonania funkcji {func.__name__}: {execution_time}')
        return result

    return wrapper


@measure_time
def my_function():
    """Dokumentacja"""
    pass


@measure_time
def my_wait():
    time.sleep(2)


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print('Sum is:', suma)


@measure_time
def my_sum_without_for():
    total = sum(range(15_000_000))
    print("Sum is:", total)


@measure_time
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Sum is:", total)


print(my_function.__doc__)  # Dokumentacja
# my_function()  # Czas wykonania funkcji my_function: 0.0
# my_wait()  # Czas wykonania funkcji my_wait: 2.0014569759368896
my_for_sum()  # Czas wykonania funkcji my_for_sum: 0.7350516319274902
my_sum_without_for()  # Czas wykonania funkcji my_sum_without_for: 0.5828125476837158
my_sum_np()  # Czas wykonania funkcji my_sum_np: 0.04200005531311035
