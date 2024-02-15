#1
# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))

# for num in range(start, end + 1):
#     if num % 7 == 0:
#         print(num)


#2
# start = int(input("Введіть початок діапазону: "))
# end = int(input("Введіть кінець діапазону: "))

# # Вивести всі числа діапазону
# print("Всі числа діапазону:")
# for num in range(start, end + 1):
#     print(num, end=" ")

# print("\n")

# # Вивести всі числа діапазону в спадному порядку
# print("Всі числа діапазону в спадному порядку:")
# for num in range(end, start - 1, -1):
#     print(num, end=" ")

# print("\n")

# # Вивести всі числа, кратні 7
# print("Всі числа, кратні 7:")
# for num in range(start, end + 1):
#     if num % 7 == 0:
#         print(num, end=" ")

# print("\n")

# # Порахувати кількість чисел, кратних 5
# count_multiples_of_5 = 0
# for num in range(start, end + 1):
#     if num % 5 == 0:
#         count_multiples_of_5 += 1

# print("Кількість чисел, кратних 5:", count_multiples_of_5)


#3
start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
