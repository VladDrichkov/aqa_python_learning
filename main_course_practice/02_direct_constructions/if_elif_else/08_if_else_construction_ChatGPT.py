# Задача 1. Допуск к запуску автотестов

environment = "stage"
is_admin = False
has_token = True
maintenance = False

environment = "stage"
is_admin = False
has_token = True
maintenance = True

environment = "stage"
is_admin = False
has_token = True
maintenance = True

environment = "prod"
is_admin = True
has_token = False
maintenance = True

environment = "prod"
is_admin = False
maintenance = False
has_token = True

# maintenance = True режим техобслуживания включен

access_allowed = "доступ разрешен"
access_denied = "доступ запрещен"

if is_admin:
    print(access_allowed)
elif maintenance:
    print(access_denied)
elif (environment == "stage" or environment == "test") and has_token:
    print(access_allowed)
else:
    print(access_denied)

# =========================================================================
# Задача 4. Найди логическую ошибку

duration_ms = 750

# if duration_ms > 300:
#     print("Медленный")
# elif duration_ms > 600:
#     print("Очень медленный")
# elif duration_ms > 1000:
#     print("Критически медленный")
# else:
#     print("Нормальный")

# медленный
# медленный
# все кроме первой если больше 300 и else если меньше или равно

if duration_ms > 1000:
    print("Критически медленный")
elif duration_ms > 600:
    print("Очень медленный")
elif duration_ms > 300:
    print("Медленный")
else:
    print("Нормальный")

#======================== Задача 3. Решение о повторном запуске теста
print("======================== Задача 3. Решение о повторном запуске теста===========")

status = "failed"
attempt = 4
max_attempts = 3
is_critical = True

if status == "skipped":
    print("Пропущен")
elif status == "passed":
    print("Завершен успешно")
elif status == "failed" and attempt < max_attempts:
    print("Повторить тест")
elif is_critical:
    print("Остановить прогон")
else:
    print("Зафиксировать ошибку")


# Задача 2. Классификация ответа API

print(" =============Задача 2. Классификация ответа API=========")
status_code = 604
has_body = True

if 500 <=  status_code <= 599:
    print("Ошибка сервера")
elif 400 <= status_code <= 499 and has_body:
    print("Ошибка клиента с описанием")
elif 400 <= status_code <= 499:
    print("Ошибка клиента без описания")
elif 200 <= status_code <= 299:
    print("успешный ответ")
else:
    print("неизвестный статус")

# задача 5: проверка конфигурации
print("=============задача 5: проверка конфигурации=====================")

browser = "safari"
headless = True
resolution = "1920x1080"

# browser = "chrome"
# headless = False
# resolution = "какое угодно"

is_browser_support = (
            browser in ("chrome", "firefox") or
            browser == "safari" and not headless)

print(f"is_support: {is_browser_support}")

is_resolution_requirement = resolution in ("1920x1080", "1366x768") or not headless

if is_browser_support and is_resolution_requirement:
    print("Конфигурация допустима")
else:
    print("Конфигурация недопустима")

# if is_browser_support and headless:
#     if resolution == "1920x1080" or resolution == "1366x768":
#         print("Конфигурация допустима")
#     else:
#         print("Конфигурация недопустима")
# elif is_browser_support:
#     print("Конфигурация допустима")
# else:
#     print("Конфигурация недопустима")


# Дополнительная задача. Проверка готовности автотеста к запуску
print("================Дополнительная задача. Проверка готовности автотеста к запуску==========")

environment = "stage"
has_token = True
test_data_loaded = True
browser = "chrome"
headless = True

is_environment_enable = ((environment in ("stage", "prod") and has_token) or
                         environment == "test")

if browser == "firefox" and headless:
    is_browser_support = environment in ("test", "stage")
elif browser in ("firefox", "chrome"):
    is_browser_support = True
else:
    is_browser_support = False

if is_environment_enable and is_browser_support and test_data_loaded:
    print("Тест готов к запуску")
else:
    print("Запуск запрещен")

# Задача 6. Приоритет ошибок
print("=================Задача 6. Приоритет ошибок=====================")

status_code = 200
response_time = 3200
has_required_fields = True

if status_code < 200 or status_code >= 300:
    print("неверный статус")
elif not has_required_fields:
    print("неверная структура")
elif response_time > 2000:
    print("Превышено время ответа")
else:
    print("Тест пройден")

# Задача 7. Доступ к тестовому стенду
print("=====================Задача 7. Доступ к тестовому стенду===============")

role = "qa"
environment = "prod"
has_vpn = True
has_approval = False
working_hours = True

# if role == "developer":
#     is_prod_enable = False
# elif role == "qa" and has_vpn and has_approval and working_hours:
#     is_prod_enable = True
# elif role == "admin" and has_vpn:
#     is_prod_enable = True

is_test_enable = role in ("qa", "developer")
is_stage_enable = role in ("qa", "developer") and has_vpn
is_prod_enable = (
        (role == "qa" and has_vpn and has_approval and working_hours) or
        (role == "admin" and has_vpn)
)

access_allowed = (
    (environment == "prod" and is_prod_enable) or
    (environment == "test" and is_test_enable) or
    (environment == "stage" and is_stage_enable)
)

if access_allowed:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

#========== Задача 8. Допуск релиза к деплою=========

environment = "prod"          # "test", "stage", "prod"
branch = "release"            # "develop", "feature", "release", "hotfix"
role = "qa"                   # "qa", "devops"
tests_passed = True           # True, False
has_approval = True           # True, False
is_hotfix = False             # True, False
service_available = True      # True, False



