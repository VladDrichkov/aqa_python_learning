# Задача 1 — polling статуса API
print("================Задача 1 — polling статуса API==================")
statuses = ["processing", "processing", "processing", "ready"]

count = 0
index = 0

while True:
    count += 1
    if statuses[index] == "ready":
        print(f"status: {statuses[index]}")
        print(f"checks: {count}")
        break
    index += 1

# Задача 2 — ограниченное количество polling-проверок
print("==================# Задача 2 — ограниченное количество polling-проверок===========")
statuses = [
    # "processing",
    # "processing",
    # "processing",
    # "processing",
    # "ready"
]

checks = 0
index = 0
final_status = "no_status"
while index < len(statuses) and checks < 3:
    checks += 1
    final_status = statuses[index]
    if statuses[index] == "ready":
        break
    index += 1

print(checks)
print(f"index: {index}")
print(f"final status: {final_status}")
print(f"checks: {checks}")

# Задача 3 — retry с двумя причинами остановки
print("==================Задача 3 — retry с двумя причинами остановки===========")
status_codes = [500, 502,
                503, 300, 500
                ]

index = 0
checks = 0
final_status = "no_status"
while index < len(status_codes) and checks < 4:
    checks += 1
    final_status = status_codes[index]
    if status_codes[index] == 200:
        break
    index += 1

print(index)
print(f"final_status: {final_status}")
print(f"checks: {checks}")
print("success" if final_status == 200 else "failed")
