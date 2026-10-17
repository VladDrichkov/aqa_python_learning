## Задание 1. Процент пройденных

# Написать функцию, которая принимает количество пройденных тестов
# и общее количество, а возвращает процент.
#
# Проверить на 18 из 20.

def pass_rate(test_numbers, test_total):
    return test_numbers * 100 / test_total

print(pass_rate(18, 20))


## Задание 3. Первый провал
#
# Написать функцию, которая принимает список статусов
# и возвращает номер первого проваленного теста.
# Если провалов нет — вернуть `None`.
#
# ```Python
# statuses = ["пройден", "пройден", "провален", "пройден"]
# ```
#
#
# Нумерация с нуля, так что ответ здесь — `2`.

def get_first_failed(statuses):
    for index, status in enumerate(statuses, 0):
        if status == "провален":
            return index
    return None

statuses = ["пройден", "пройден", "провален", "пройден"]
print(get_first_failed(statuses))

## Задание 4. Разброс оценок
# Написать функцию, которая принимает список чисел и
# возвращает сразу три значения: минимум, максимум и разницу между ними.
#

scores = [72, 95, 58, 88]

def score_report(scores):
    min_value = scores[0]
    max_value = scores[0]

    for score in scores:
        if score > max_value:
            max_value = score
        if score < min_value:
            min_value = score
    return min_value, max_value, max_value - min_value

low, high, difference = score_report(scores)
print(low, high, difference)

