# Задание 1. Сумма списка
# Посчитать сумму всех чисел и напечатать результат.
numbers = [5, 8, 2, 4, 7]
total = 0
for num in numbers:
    total += num
print(total)

# или через sum
total = sum(numbers)

# Задание 2. Первый и последний
# Напечатать первый и последний элементы списка, не зная его длины заранее.
print("#=================== Задание 2. Первый и последний=========")
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])

# Задание 3. Убрать все бананы
# Из списка убрать все бананы. Результат напечатать.
print("#=================Задание 3. Убрать все бананы==============")
print("удаление проходом с конца")

fruits = ["яблоко", "банан", "груша", "банан", "киви"]

fruits_clear = fruits.copy()
for index in range(len(fruits)-1, -1, -1):
    if fruits[index] == "банан":
        fruits_clear.pop(index)

print(fruits_clear)

print("удаление значение на месте двумя указателями")
write_index = 0
for read_index in range(len(fruits)):
    if fruits[read_index] != "банан":
        fruits[write_index] = fruits[read_index]
        write_index += 1
del fruits[write_index:]
print(fruits)

print("удаление через генератор списков")
clean = [fruit for fruit in fruits if fruit != "банан"]
print(clean)

# Задание 4. Самое большое число
print("#=============== Задание 4. Самое большое число============")
numbers = [3, 17, 8, 42, 5]

max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)

## Задание 5. Найди ошибку
# Программа должна напечатать все элементы списка. Что произойдёт на самом деле?

