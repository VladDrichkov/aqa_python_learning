from unittest import result


# Задача: отбор проблемных автотестов
# Есть словарь run_data с результатами тестового прогона.
# run_data = {
#         "suites": [
#             {
#                 "name": "auth",
#                 "tests": [
#                     {"name": "login", "status": "passed", "duration_ms": 180, "retries": 0},
#                     {"name": "logout", "status": "failed", "duration_ms": 620, "retries": 1},
#                     {"name": "refresh", "status": "failed", "duration_ms": None, "retries": 2},
#                 ],
#             },
#             {
#                 "name": "payments",
#                 "tests": [
#                     {"name": "create_payment", "status": "passed", "duration_ms": 910, "retries": 0},
#                     {"name": "refund", "status": "skipped", "retries": 0},
#                     {"name": "logout", "status": "failed", "duration_ms": 700, "retries": 0},
#                 ],
#             },
#             {
#                 "name": "empty_suite",
#                 "tests": [],
#             },
#         ]
#     }
#
# Внутри него находятся test suites, а в каждой suite — список тестов.
#
# Нужно написать функцию:
#
# analyze_tests(run_data, predicate)
#
# predicate — функция, которая получает один словарь теста
# и возвращает True или False.
#
# Функция analyze_tests() должна пройти по всем suite
# и вернуть словарь со структурой:
#
# {
#     "matched": [...],
#     "count": ...,
#     "suites": {...}
# }
#
# Требования к результату:
#
# - matched — список строк вида "suite_name::test_name"
#   для тестов, которые прошли predicate;
#
# - count — общее количество таких тестов;
#
# - suites — словарь вида:
#   {suite_name: количество_совпадений};
#
# - suite с нулём совпадений в suites добавлять не нужно.
#
# Нужно выполнить два запуска функции.
#
# 1. Передать обычную именованную функцию-predicate,
#    которая выбирает только failed-тесты,
#    у которых был хотя бы один retry.
#
# 2. Передать lambda,
#    которая выбирает тесты с duration_ms > 600.
#
# Граничные случаи:
#
# - duration_ms может быть равен None;
# - ключ duration_ms может вообще отсутствовать;
# - suite может содержать пустой список tests;
# - одинаковые имена тестов могут встречаться в разных suite —
#   это разные тесты;
# - retries = 0 является полноценным значением
#   и не должно трактоваться как отсутствие данных.
#
# Ограничение:
#
# - пока не используй comprehensions;
# - не используй generator expressions;
# - не используй filter();
# - решай через обычные циклы и управляющие конструкции.


def is_fail_test_with_retry(test):
    if test["status"] == "failed" and test["retries"] > 0:
        return True
    return False




def analyze_tests(run_data, predicate):
    result = {
        "matched": [],
        "count": 0 ,
        "suites": {}
    }

    for suite in run_data["suites"]:
        suite_count = 0
        for test in suite["tests"]:
            if predicate(test):
                result["matched"].append(f"{suite["name"]}::{test["name"]}")
                suite_count += 1
        if suite_count > 0:
            result["suites"][suite["name"]] = suite_count

    result["count"] = len(result["matched"])

    return result


def get_failed_tests(run_data):
    result = [
        f"{suite["name"]}::{test["name"]}"
        for suite in run_data["suites"]
        for test in suite["tests"]
        if test["status"] == "failed"
    ]
    return result


def build_test_result(run_data):
    return [
        f"{test["name"]}:: OK"
        if test["status"] == "passed"
        else f"{test["name"]}:: NOT OK"
        for suite in run_data["suites"]
        for test in suite["tests"]
    ]


def build_test_duration_report(run_data):
    return [
        f"{suite["name"]}::{test["name"]} - SLOW"
        if test["duration_ms"] > 600
        else f"{suite["name"]}::{test["name"]} - NORMAL"
        for suite in run_data["suites"]
        for test in suite["tests"]
        if "duration_ms" in test
        if test["duration_ms"] is not None
    ]

def main():
    run_data = {
        "suites": [
            {
                "name": "auth",
                "tests": [
                    {"name": "login", "status": "passed", "duration_ms": 180, "retries": 0},
                    {"name": "logout", "status": "failed", "duration_ms": 620, "retries": 1},
                    {"name": "refresh", "status": "failed", "duration_ms": None, "retries": 2},
                ],
            },
            {
                "name": "payments",
                "tests": [
                    {"name": "create_payment", "status": "passed", "duration_ms": 910, "retries": 0},
                    {"name": "refund", "status": "skipped", "retries": 0},
                    {"name": "logout", "status": "failed", "duration_ms": 700, "retries": 0},
                ],
            },
            {
                "name": "empty_suite",
                "tests": [],
            },
        ]
    }

    failed_test_with_result = analyze_tests(run_data, is_fail_test_with_retry)

    tests_with_durations = analyze_tests(
        run_data,
        lambda test: test.get("duration_ms", 0) is not None and test.get("duration_ms", 0) > 600)
    #
    # print("================analyze_result=================\n")
    # for k,v in failed_test_with_result.items():
    #     print(k)
    #     print(v)
    #
    # print("================analyze_result=================\n")
    #
    # for k,v in tests_with_durations.items():
    #     print(k)
    #     print(v)
    #

    run_data = {
        "suites": [
            {
                "name": "auth",
                "tests": [
                    {"name": "login", "status": "passed", "duration_ms": 180},
                    {"name": "logout", "status": "failed", "duration_ms": 720},
                    {"name": "refresh", "status": "failed", "duration_ms": None},
                ],
            },
            {
                "name": "payments",
                "tests": [
                    {"name": "create_payment", "status": "passed", "duration_ms": 950},
                    {"name": "refund", "status": "skipped"},
                    {"name": "cancel_payment", "status": "failed", "duration_ms": 430},
                ],
            },
            {
                "name": "profile",
                "tests": [
                    {"name": "get_profile", "status": "passed", "duration_ms": 310},
                    {"name": "update_profile", "status": "failed", "duration_ms": 810},
                ],
            },
        ]
    }

    # print("===================================================\n")
    #
    # failed_tests = get_failed_tests(run_data)
    # print(failed_tests)
    #
    # print("======================build_tests_result")
    # tests_result = build_test_result(run_data)
    # print(tests_result)

    test_duration_report = build_test_duration_report(run_data)
    print(test_duration_report)


if __name__ == '__main__':
    main()




