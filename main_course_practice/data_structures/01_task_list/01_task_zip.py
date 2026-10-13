# Задача 2. Словарь из двух списков
# Из списка городов и списка стоимостей доставки собрать словарь, где город — ключ, а стоимость — значение.

cities = ["Москва", "Казань", "Сочи"]
prices = [0, 400, 500]
result_delivery = dict(zip(cities, prices, strict=True))

# для контроля несовпадения длин списков можно использовать strict

fruits = ["яблоко", "банан", "банан", "банан"]
# print(fruits)

for i in range(len(fruits)-1,-1, -1):
    print(fruits[i])
    if fruits[i] == "банан":
        fruits.pop(i)
print(fruits)
