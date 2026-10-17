# Что такое функция?

def hello(name):
    print(f"Привет: {name}!")

hello("Vlad")

## Задание 3. Проверка диапазона
#
# Написать функцию, которая принимает число и границу, а печатает,
# укладывается ли число в границу.
# Вызвать так, чтобы на экране оказалось:
# 80 не больше 100
# 150 больше 100

def check_numeric_boundary(number, threshold):
    if number <= threshold:
        print(f"{number} не больше {threshold}")
    else:
        print(f"{number} больше {threshold}")

check_numeric_boundary(80, 100)
check_numeric_boundary(150, 100)

## Задание 4. Убрать повтор
# Программа считает стоимость трёх заказов со скидкой. Свернуть повторяющийся кусок в функцию.

# total = 5000
# discount = total * 10 / 100
# print("Заказ:", total, "скидка:", discount, "к оплате:", total - discount)
#
#
# total = 3000
# discount = total * 10 / 100
# print("Заказ:", total, "скидка:", discount, "к оплате:", total - discount)
#
#
# total = 1200
# discount = total * 10 / 100
# print("Заказ:", total, "скидка:", discount, "к оплате:", total - discount)

def payment(total):
    discount = total * 10 / 100
    print("Заказ:", total, "скидка:", discount, "к оплате:", total - discount)

payment(1200)
