## Задание 1. Скидка с умолчанием

# Написать функцию, которая считает скидку от суммы.
# Процент по умолчанию — 10, но его можно задать другим.
#
# Проверить на сумме 5000 с обычной скидкой и со скидкой 20%.

def calculate_discount(total, discount_percentage=10):
    return total * discount_percentage / 100

print(calculate_discount(5000))
print(calculate_discount(5000, 20))


def add_failure(name, failures=None):
    if failures is None:
        failures = []
    failures.append(name)
    return failures

## Задание 3. Читаемый вызов

# Дана функция с четырьмя параметрами:

def make_case(name, browser="chrome", retries=1, critical=False):
    print(name, browser, retries, critical)

# Вызвать её так, чтобы
# тест назывался «оплата»,
# повторов было 3,
# тест считался критичным,
# а браузер остался по умолчанию.

make_case(
    "оплата",
    retries=3,
    critical=True
)

## Задание 4. Среднее из чего угодно

# Написать функцию, которая принимает любое количество оценок и возвращает среднее.
# Если оценок не передали — вернуть 0.

def calculate_average(*score):
    if len(score) == 0:
        return 0
    return sum(score) / len(score)

print(calculate_average())

## Задание 5. Карточка теста

# Написать функцию, которая принимает
# имя теста и любое количество дополнительных полей, а печатает их списком.
#
# Вызвать так, чтобы получилось:
# Тест: оплата
#    browser = firefox
#    retries = 3

def build_report(test_name, **kwargs):
    print(f"Тест: {test_name}")
    for k,v in kwargs.items():
        print(f"\t{k} = {v}")

build_report("оплата", browser="firefox", retries=3)
