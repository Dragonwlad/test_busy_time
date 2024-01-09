import time

import numpy as np

numbers = list(np.random.randint(low=1, high=10, size=100000))

'''В предложенном решение на выполнение уходит
в среднем от 12 до 17 секунд :  12.874617338180542 , 17.295258283615112'''
start_time = time.time()
for i, number in enumerate(numbers):
    number_is_in_tail = number in numbers[i+1:]
end_time = time.time()

elapsed_time = end_time - start_time
print('Исходное время выполнения: ', elapsed_time)


'''Решение по индексам результат - '''
# Для проверки работоспособности небольшой список
# numbers = (2, 4, 6, 7, 8, 10, 11, 20, 30, 55, 2, 10, 11)


def binary_search(arr, x, low):
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return True
    return False


start_time = time.time()

numbers = sorted(numbers)
for i, number in enumerate(numbers):
    binary_search(arr=numbers, low=i+1, x=number)

end_time = time.time()

elapsed_time = end_time - start_time
print('Время выполнения с доработками: ', elapsed_time)

# Ускорение ~ в 100 раз: 0.12065720558166504
