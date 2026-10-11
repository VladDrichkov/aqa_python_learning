responses = [
    {"status": 503, "request_time_ms": 400, "retry_after_ms": 500},
    {"status": 429, "request_time_ms": 300, "retry_after_ms": 1200},
    {"status": 503, "request_time_ms": 700, "retry_after_ms": 800},
    {"status": 200, "request_time_ms": 900, "retry_after_ms": 0},
    {"status": 500, "request_time_ms": 400, "retry_after_ms": 0},
]

max_attempts = 4
timeout_ms = 5000

attempts = 0
index = 0
elapsed_time = 0
final_status = None
result = "responses_exhausted"

while index < len(responses):
    attempts += 1
    elapsed_time += responses[index]["request_time_ms"]
    final_status = responses[index]["status"]

    if elapsed_time > timeout_ms:
        result = "timeout"
        break
    if final_status == 200:
        result = "success"
        break
    if final_status == 400:
        result = "client_error"
        break
    if final_status == 500:
        result = "server_error"
        break

    if attempts >= max_attempts:
        result = "max_attempts_exhausted"
        break
    if index + 1 >= len(responses):
        break
    if elapsed_time + responses[index]["retry_after_ms"] > timeout_ms:
        result = "timeout"
        break
    elapsed_time += responses[index]["retry_after_ms"]
    index += 1

print(f"attempts: {attempts}")
print(f"elapsed_time: {elapsed_time}")
print(f"final_status: {final_status}")
print(f"result: {result}")

