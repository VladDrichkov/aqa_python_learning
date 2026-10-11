status_codes = [
    500,
    502,
    # 200,
    503,
    504
]

result = "responses_exhausted"
attempts = 0
final_status = None
index = 0

while index < len(status_codes):
    attempts += 1
    final_status = status_codes[index]
    if final_status == 200:
        result = "success"
        break
    if final_status == 400:
        result = "client_error"
        break
    if attempts >= 4:
        result = "failed"
        break
    index += 1

print(f"attempts: {attempts}")
print(f"final_status: {final_status}")
print(f"result: {result}")
