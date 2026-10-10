statuses = [
    "processing",
    "processing",
    "ready",
    "processing"
]

index = 0
checks = 0
final_status = None
while index < len(statuses):
    checks += 1
    final_status = statuses[index]
    if statuses[index] == "ready":
        break
    index += 1

print(f"checks: {checks}")
print(f"final_status: {final_status}")
