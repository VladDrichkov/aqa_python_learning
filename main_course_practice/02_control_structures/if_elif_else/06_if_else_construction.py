# Задание 1. Оценка по баллам
from unittest import result

score = 95

if score >= 90:
    print("отлично")
elif score >= 70:
    print("хорошо")
elif score >= 50:
    print("удовлетворительно")
else :
    print("неудовлетворительно")

# Задание 2. Стоимость доставки
print("===============Задание 2. Стоимость доставки=============")
city = "Москва"

if city == "Москва":
    print("стоимость доставки 0 руб.")
elif city == "Санкт-Петербург":
    print("стоимость доставки 300 руб.")
elif city == "Казань":
    print("стоимость доставки 400 руб.")
else:
    print("стоимость доставки 500 руб.")

# Задание 3. Итог заказа со скидкой
print("=================== Задание 3. Итог заказа со скидкой ===============")

total = 4500

if total >= 5000:
    discount = 10 * total / 100
elif total >= 3000:
    discount = 5 * total / 100
else:
    discount = 0
total_payment = total - discount
print(f"скидка: {discount}")
print(f"сумма к оплате: {total_payment}")