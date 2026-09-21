delivery_cities = ["Москва", "Санкт-Петербург", "Казань", "Сочи"]
city = "Казань"

if city in delivery_cities:
    print("доставка есть")
if city not in delivery_cities:
    print("доставки нет")