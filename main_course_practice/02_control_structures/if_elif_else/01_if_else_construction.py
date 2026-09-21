temperature = int(input("Введите температуру: "))

if temperature < 0:
    print("холодно")
if temperature == 0:
    print("на нуле")
if 1 <= temperature <= 20:
    print("прохладно")
if temperature > 20:
    print("тепло")

