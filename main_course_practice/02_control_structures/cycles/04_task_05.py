responses = [
    {"state": "processing", "request_time_ms": 450, "retry_after_ms": 700},
    {"state": "processing", "request_time_ms": 600, "retry_after_ms": 900},
    {"state": "processing", "request_time_ms": 800, "retry_after_ms": 1200},
    {"state": "completed",  "request_time_ms": 500, "retry_after_ms": 0},
    {"state": "failed",     "request_time_ms": 300, "retry_after_ms": 0},
]

max_attempts = 6
timeout_ms = 5000

index = 0
elapsed_time = 0
result = "responses_exhausted"
final_state = None
attempts = 0

while index < len(responses):
    attempts += 1
    final_state = responses[index]["state"]
    elapsed_time += responses[index]["request_time_ms"]
    if elapsed_time > timeout_ms:
        result = "timeout"
        break
    if final_state == "completed":
        result = "success"
        break
    elif final_state == "failed":
        result = "failed"
        break
    elif index + 1 >= len(responses):
        result = "responses_exhausted"
        break
    elif attempts >= max_attempts:
        result = "max_attempts_exhausted"
        break
    elif elapsed_time + responses[index]["retry_after_ms"] > timeout_ms:
        result = "timeout"
        break

    elapsed_time += responses[index]["retry_after_ms"]
    print(f"attempts: {attempts}; elapsed_time: {elapsed_time}")
    index += 1

print(f"attempts: {attempts}")
print(f"elapsed_time: {elapsed_time}")
print(f"final_state: {final_state}")
print(f"result: {result}")