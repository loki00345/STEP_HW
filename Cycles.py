
#1
# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))

# sum_even = 0
# sum_odd = 0
# sum_multiple_9 = 0
# count_even = 0
# count_odd = 0
# count_multiple_9 = 0

# for num in range(start, end + 1):
#     # Парні числа
#     if num % 2 == 0:
#         sum_even += num
#         count_even += 1
#     # Непарні числа
#     else:
#         sum_odd += num
#         count_odd += 1
#     # Числа, кратні 9
#     if num % 9 == 0:
#         sum_multiple_9 += num
#         count_multiple_9 += 1

# average_even = sum_even / count_even if count_even != 0 else 0
# average_odd = sum_odd / count_odd if count_odd != 0 else 0
# average_multiple_9 = sum_multiple_9 / count_multiple_9 if count_multiple_9 != 0 else 0

# print("Сума парних чисел:", sum_even)
# print("Середнє парних чисел:", average_even)
# print("Сума непарних чисел:", sum_odd)
# print("Середнє непарних чисел:", average_odd)
# print("Сума чисел, кратних 9:", sum_multiple_9)
# print("Середнє чисел, кратних 9:", average_multiple_9)


#2
# length = int(input("Введіть довжину лінії: "))
# symbol = input("Введіть символ для заповнення лінії: ")

# for i in range(length):
#     print(symbol)

#3
# while True:
#     number = float(input("Введіть число (для завершення введіть 7): "))
    
#     match number:
#         case 7:
#             print("Good bye!")
#             break
#         case _ if number > 0:
#             print("Number is positive")
#         case _ if number < 0:
#             print("Number is negative")
#         case _:
#             print("Number is equal to zero")


#4
numbers = []
while True:
    number = input("Введіть число (для завершення введіть 7): ")
    
    if number == '7':
        print("Good bye!")
        break
    
    numbers.append(float(number))

if numbers:
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print("Сума введених чисел:", total)
    print("Максимальне число:", maximum)
    print("Мінімальне число:", minimum)
else:
    print("Ви не ввели жодного числа.")
