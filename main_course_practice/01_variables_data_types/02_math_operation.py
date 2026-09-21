from math import ceil


def main():
    # total_tests = 37
    # workers = 5
    # group_amount = total_tests // workers
    # print(group_amount)
    # tests_residue = total_tests % workers
    # print(tests_residue)
    #
    # failed_attempts = 14
    # retry_batch = 3
    #
    # full_groups = failed_attempts // retry_batch
    # remaining_attempts = failed_attempts % retry_batch
    #
    # total_retries = full_groups + 1
    # print(f"full_groups: {full_groups}")
    # print(f"remaining_attempts: {remaining_attempts}")
    # print(f"total_retries: {total_retries}")

    # total_tests = 73
    # failed_tests = 8
    # workers = 6
    # expected_duration = 120.0
    # actual_duration = 127.5
    #
    # passed_tests = total_tests - failed_tests
    # failed_tests_ratio = (failed_tests / total_tests) * 100
    # abs_duration_deviation = round(abs(expected_duration - actual_duration), 1)
    # full_groups = total_tests // workers
    # remaining_tests = total_tests % workers
    #
    # print(abs_duration_deviation)

    # total_tests = 137
    # failed_tests = 11
    # flaky_tests = 6
    # workers = 8
    #
    # expected_duration = 240.0
    # actual_duration = 258.7
    #
    # max_failed_percent = 10
    # max_duration_deviation_percent = 8
    #
    # passed_tests = total_tests - (failed_tests + flaky_tests)
    # failed_percent = round((failed_tests / total_tests) * 100, 2)
    # flaky_percent = round((flaky_tests / total_tests) * 100, 2)
    # duration_difference = round(abs(expected_duration - actual_duration), 1)
    # duration_deviation_percent = round((duration_difference / expected_duration) * 100, 2)
    # tests_per_worker = total_tests // workers
    # workers_with_extra_test = total_tests % workers
    # failed_rate_ok = failed_percent <= max_failed_percent
    # duration_ok = duration_deviation_percent <= max_duration_deviation_percent
    #
    # print(f"passed_tests: {passed_tests:}")
    # print(f"failed_percent :{failed_percent}")
    # print(f"flaky_percent :{flaky_percent}")
    # print(f"duration_difference :{duration_difference}")
    # print(f"duration_deviation_percent :{duration_deviation_percent}")
    # print(f"tests_per_worker :{tests_per_worker}")
    # print(f"workers_with_extra_test :{workers_with_extra_test}")
    # print(f"failed_rate_ok :{failed_rate_ok}")
    # print(f"duration_ok :{duration_ok}")

    # total_tests = 103
    # max_tests_per_worker = 15
    # max_workers = 6
    #
    # required_workers = ceil(total_tests / max_tests_per_worker)
    # has_enough_workers = required_workers <= max_workers
    #
    # max_allocatable_tests = min(max_workers * max_tests_per_worker, total_tests)
    # unallocated_tests = abs(total_tests - max_allocatable_tests)

    # max_retries = 3
    # attempts_made = 3
    #
    # retries_used = attempts_made - 1
    # remaining_retries = max_retries - retries_used
    # can_retry = remaining_retries > 0

    # Задача 6 — валидация превышения retry-лимита
    #
    # Дано:
    # max_retries = 3
    # attempts_made = 6
    #
    # Условия:
    # Первая попытка — обычный запуск теста, не retry.
    # Каждая следующая попытка после неуспешной считается retry.
    # Все 6 зафиксированных попыток завершились failed.
    # После первой попытки разрешено максимум max_retries повторных попыток.
    # Система должна была остановиться после исчерпания retry-лимита,
    # но из-за дефекта продолжила выполнение.
    #
    # Нужно вычислить:
    # retries_used — сколько retry фактически было выполнено.
    # max_allowed_attempts — сколько попыток максимум разрешено конфигурацией.
    # attempts_limit_exceeded — превышен ли лимит попыток.
    # extra_attempts — на сколько попыток лимит превышен.
    # remaining_retries — сколько retry осталось, не допуская отрицательного значения.
    # can_retry — можно ли выполнить ещё один retry по конфигурации.
    #
    # Ограничение:
    # Решить без if.
    # Решение должно быть компактным.

    max_retries = 3
    attempts_made = 6

    retries_used = attempts_made - 1
    max_allowed_attempts = 1 + max_retries
    attempts_limit_exceeded = attempts_made > max_allowed_attempts
    extra_attempts = max((attempts_made - max_allowed_attempts), 0)
    remaining_retries = max((max_retries - retries_used), 0)
    can_retry = (max_retries - retries_used) > 0

    print(f"retries_used: {retries_used}")
    print(f"max_allowed_attempts: {max_allowed_attempts}")
    print(f"attempts_limit_exceeded: {attempts_limit_exceeded}")
    print(f"extra_attempts: {extra_attempts}")
    print(f"remaining_retries: {remaining_retries}")
    print(f"can_retry: {can_retry}")

if __name__ == '__main__':
    main()
