## Задача 3. Отчёт по прогону
# Результаты прогона приходят списком словарей — так их отдают почти все инструменты.
# Напечатать имена проваленных тестов и сколько тестов в каждом статусе.

runs = [
    {"test": "login", "status": "пройден", "browser": "chrome"},
    {"test": "cart", "status": "провален", "browser": "chrome"},
    {"test": "login", "status": "провален", "browser": "firefox"},
    {"test": "pay", "status": "пройден", "browser": "firefox"},
]

failed_tests = []
test_counts = {}

for run in runs:
    if run["status"] == "провален":
        failed_tests.append(run["test"])
    test_counts[run["status"]] = test_counts.get(run["status"], 0) + 1

print(failed_tests)
print(test_counts)

## Задача 4. Разложить по категориям
# Два связанных списка: товары и категории, к которым они относятся.
# Собрать словарь, где ключ — категория, а значение — список товаров этой категории.
# Ожидаемый результат:
# {'молочное': ['молоко', 'сыр', 'кефир'], 'выпечка': ['хлеб', 'батон']}

print("================## Задача 4. Разложить по категориям============")

products = ["молоко", "хлеб", "сыр", "батон", "кефир"]
categories = ["молочное", "выпечка", "молочное", "выпечка", "молочное"]

products_by_categories = {}

for index, category in enumerate(categories, 0):
    products_list = products_by_categories.setdefault(category, [])
    products_list.append(products[index])

print(products_by_categories)

## Задача 5. Кто падает чаще всех
# Дан список упавших тестов за неделю. Одно имя — одно падение.
# Напечатать имя теста, который падал чаще остальных, и сколько раз он упал.
print("==========## Задача 5. Кто падает чаще всех==============")

failures = ["login", "cart", "login", "pay", "login", "cart"]

failure_counts = {}
for test in failures:
    failure_counts[test] = failure_counts.get(test, 0) + 1
print(failure_counts)

failure_counts = sorted(
    failure_counts.items(),
    key=lambda item: item[1],
    reverse=True
)
max_failure_test = failure_counts[0][0]
max_failure = failure_counts[0][1]

# max_failure_test = ""
# max_failure = 0
# for k,v in failure_counts.items():
#     if v > max_failure:
#         max_failure = v
#         max_failure_test = k

print(max_failure_test)
print(max_failure)



