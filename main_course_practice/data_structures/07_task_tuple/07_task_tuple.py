test_results = (
    ("login", 200, 180),
    ("payment", 503, 920),
    ("profile", 200, 410),
    ("search", 404, 250),
    ("orders", 500, 780),
)


problem_tests =[]
for test_name, status, duration_ms in test_results:
    if status < 400:
        continue
    problem_tests.append(
        f"{test_name} | status={status} | duration={duration_ms}"
    )
print(problem_tests)

slow_tests = [
    test_name
    for test_name, status, duration_ms in test_results
    if duration_ms > 600
]
print(slow_tests)

first_server_error = None
for test in test_results:
    if test[1] >= 500:
        first_server_error = test
        break
print(f"first_server_error: {first_server_error}")

if first_server_error is not None:
    server_error_name, server_error_status, server_error_duration = first_server_error
else:
    server_error_name, server_error_status, server_error_duration =(None, None, None)

print(f"server_error_name: {server_error_name}")
print(f"server_error_status: {server_error_status}")
print(f"server_error_duration: {server_error_duration}")
