# Задача 4 — retry с накоплением времени
#
# Есть ответы API:
#
# responses = [
#     {"status": 503, "time_ms": 450},
#     {"status": 500, "time_ms": 700},
#     {"status": 200, "time_ms": 1200},
#     {"status": 200, "time_ms": 600},
# ]
#
# Автотест повторяет запросы последовательно.
#
# Успешным результат считается только ответ, у которого одновременно выполняются два условия:
#
# status == 200
# time_ms <= 1000
#
# Третий ответ:
#
# {"status": 200, "time_ms": 1200}
#
# не является успешным, потому что время ответа превышает 1000 мс.
#
# Дополнительные ограничения:
#
# - максимум 4 попытки;
# - нужно накапливать общее время всех реально выполненных запросов;
# - если суммарное время стало больше 3000 мс, дальнейшие попытки выполнять нельзя;
# - если ответы в списке закончились, цикл должен корректно завершиться.
#
# После завершения цикла вывести:
#
# attempts: ...
# total_time: ...
# final_status: ...
# result: success / failed
#
# Для исходных данных успешным должен стать четвёртый ответ.
#

responses = [
    {"status": 503, "time_ms": 450},
    {"status": 500, "time_ms": 700},
    {"status": 200, "time_ms": 1200},
    {"status": 200, "time_ms": 600},
]

attempts = 0
total_time = 0
index = 0
final_status = None
result = "failed"

while index < len(responses) and total_time <= 3000 and attempts < 4:
    attempts += 1
    total_time += responses[index]["time_ms"]
    final_status = responses[index]["status"]
    if final_status == 200 and responses[index]["time_ms"] <= 1000:
        result = "success"
        break

    index += 1

print(f"attempts: {attempts}")
print(f"total_time: {total_time}")
print(f"final_status: {final_status}")
print(f"result: {result}")
