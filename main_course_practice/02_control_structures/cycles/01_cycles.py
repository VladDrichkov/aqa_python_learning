# Задание 1. Сумма от 1 до 10

sum = 0
for i in range(1, 11):
    sum += i
print(f"Сумма: {sum}")

# Задание 2. Только дорогие товары
print("============= # Задание 2. Только дорогие товары==========")

prices = [500, 1500, 800, 2300, 990, 1200]

for price in prices:
    if price > 1000:
        print(price)

# Задание 3. Сколько раз прибавить тройку
print("=================Задание 3. Сколько раз прибавить тройку========")
# Начинаем с нуля и прибавляем 3, пока сумма не станет больше 20.
# Напечатать, сколько раз пришлось прибавить и какая сумма получилась

count  = 0
total = 0

while True:
    result = total + 3
    if result > 20:
        break
    else:
        count += 1
        total = result
    print(f"{count}; {total}")

print(f"количество итераций: {count}")
print(f"сумма: {total}")

total = 0
count = 0
while total <= 20:

    count += 1
    total += 3
    print(f"{count}; {total}")

print(f"количество итераций: {count}")
print(f"сумма: {total}")

# Задание 4. Найди ошибку
print("================Задание 4. Найди ошибку===========")


