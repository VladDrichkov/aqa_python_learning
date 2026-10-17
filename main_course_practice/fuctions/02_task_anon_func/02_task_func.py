## Задание 1. Самые долгие тесты

# Отсортировать тесты от самого медленного к самому быстрому.
tests = [("login", 3.1), ("cart", 0.4), ("pay", 1.2), ("search", 0.9)]

sorted_by_time = sorted(tests, key=lambda test: test[1], reverse=True)
print(sorted_by_time)

## Задание 3. Отчёт по частоте падений

# Дан список пар «тест — сколько раз упал».
# Вывести по убыванию числа падений, а при равном числе — по алфавиту.

report = [("оплата", 5), ("вход", 12), ("корзина", 5)]


sorted_report = sorted(report, key=lambda test: (-test[1], test[0]))
print(sorted_report)

sorted_report_by_alphabet = sorted(report)
print(sorted_report_by_alphabet)
sorted_report_by_time = sorted(sorted_report_by_alphabet, key= lambda test: test[1], reverse=True)
print(sorted_report_by_time)


