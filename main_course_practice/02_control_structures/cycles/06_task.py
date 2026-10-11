statuses = [
    "processing",
    "processing",
    "processing",
    "ready",
    "processing"
]

index = 0
checks = 0
final_status = None

while index < len(statuses):
    if checks >= 3:
        break
    checks += 1
    final_status = statuses[index]
    if final_status == "ready":
        break
    index += 1

print(f"checks: {checks}")
print(f"final_status: {final_status}")
