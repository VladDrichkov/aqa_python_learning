## Задача 1. Максимум из трёх
#
# Напиши функцию: принимает три числа, возвращает наибольшее.
# Готовым `max` не пользуйся.
#
# Проверь на трёх наборах: `(4, 9, 1)`, `(9, 4, 1)` и `(5, 5, 5)`.

def find_max(a, b, c):
    max_value = a
    if b > a:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

print(find_max(4, 9, 1))
print(find_max(9, 4, 1))
print(find_max(5, 5, 5))

## Задача 3. Счётчик статусов
# Напиши функцию: принимает список статусов,
# возвращает словарь «статус — сколько раз встретился».

runs = ["пройден", "провален", "пройден", "пропущен", "пройден"]

def build_report(results):
    report = {}
    for result in results:
        report[result] = report.get(result, 0) + 1
    return report

print(build_report(runs))

## Задача 4. Разложить на функции

# Код работает, но делает всё сразу.
orders = [("Анна", 5000), ("Борис", 1200), ("Вера", 8000)]

def calculate_discount(total_before_discount):
    if total_before_discount >= 5000:
        discount = total * 10 / 100
    else:
        discount = 0
    return discount

def build_payment(name, total):
    discount = calculate_discount(total)
    print(name, "—", total,
          "скидка", discount,
          "к оплате", total - discount
          )

for name, total in orders:
    build_payment(name, total)

