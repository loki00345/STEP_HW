import random


def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Приклад використання функції:
# my_list = [1, 2, 3, 4, 5]
# print("Добуток елементів списку:", multiply_elements(my_list))


def find_minimum(lst):
    if len(lst) == 0:
        return None  
    min_value = lst[0]  
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

# Приклад використання функції:
# my_list = [5, 3, 8, 1, 9]
# print("Мінімум у списку:", find_minimum(my_list))


def count_primes(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for num in lst:
        if is_prime(num):
            count += 1
    return count

# Приклад використання функції:
# my_list = [i for i in range(1, 1001)]
# print("Кількість простих чисел у списку:", count_primes(my_list))


def remove_elements(lst, target):
    count_deleted = 0
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == target:
            del lst[i]
            count_deleted += 1
    return count_deleted

# Приклад використання функції:
# my_list = [1, 2, 3, 4, 5, 3, 6, 7, 3, 8]
# target = int(input("ВИДАЛИТИ ЧИСЛО: "))
# print("Кількість видалених елементів:", remove_elements(my_list, target))
# print("Список після видалення:", my_list)


def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list

# Приклад використання функції:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = merge_lists(list1, list2)
# print("Результат об'єднання списків:", result)


def power_list(lst, power):
    powered_list = [num ** power for num in lst]
    return powered_list

# Приклад використання функції:
my_list = [1, 2, 3, 4, 5]
exponent = 3
result = power_list(my_list, exponent)
print("Результат піднесення до степеня:", result)