## Задание 1. Сколько разных букв
# Дано слово. Напечатать все его разные буквы и их количество.
import copy

word = "программирование"

letters = set(word)
amount = len(letters)
print(f"letters: {letters}")
print(f"amount: {amount}")

## Задание 2. Отчёт по двум браузерам
# Даны наборы тестов, прошедших в двух браузерах.
# Напечатать четыре строки:
# что прошло в обоих браузерах,
# что только в Chrome,
# что проходило хоть где-то и
# что прошло ровно в одном.

chrome = {"login", "search", "cart", "payment"}
firefox = {"login", "cart", "profile"}

both_test_passed = chrome.intersection(firefox)
chrome_test_passed = chrome.difference(firefox)
all_test_passed = chrome.union(firefox)
only_one_test_passed = chrome.symmetric_difference(firefox)

print(both_test_passed)
print(chrome_test_passed)
print(all_test_passed)
print(only_one_test_passed)

## Задание 4. Проверка полей формы

# Даны список полей, которые форма обязана содержать,
# и список полей, которые нашлись на странице.
# Среди найденных может оказаться служебное поле `csrf` — а может и не оказаться;
# в проверке его учитывать не надо.
#
# Напечатать, совпадает ли набор целиком,
# все ли обязательные поля на месте,
# каких не хватает и какие лишние.
print("============## Задание 4. Проверка полей формы=========")
required = ["email", "password", "phone", "address"]
found = ["email", "password", "promo", "csrf"]

required_field = set(required)
found_field = set(found)
print(found_field)

cleaned_found_fields = found_field.copy()
cleaned_found_fields.discard("csrf")
print(cleaned_found_fields)

print(f"are_same: {set(found) == required_field}")
print(f"has_all_required_fields: {cleaned_found_fields.issubset(required_field)}")
print(f"missing_fields: {required_field.difference(cleaned_found_fields)}")
print(f"unexpected_fields: {cleaned_found_fields - required_field}")

## Задание 5. Есть ли повторы

# Проверить, есть ли в списке повторяющиеся значения.
# Напечатать «Есть повторы» или «Все значения разные».
print("=============Задание 5. Есть ли повторы===========")

ids = [101, 102, 103, 102, 105]
if len(ids) != len(set(ids)):
    print("есть повторы")
else:
    print("все значения разные")

# какие значения повторились

unique_items = set()
duplicates = set()

for item in ids:
    if item in unique_items:
        duplicates.add(item)
    else:
        unique_items.add(item)
print(duplicates)