test_results = (
    ("login", 200, "passed"),
    ("payment", 500, "failed"),
    ("profile", 200, "passed"),
    ("payment", 503, "failed"),
    ("logout", 200, "passed"),
)


payment_500_count = test_results.count(("payment", 500, "failed"))
print(f"payment_500_count: {payment_500_count}")
payment_503_index = test_results.index(("payment", 503, "failed"))
print(f"payment_503_index: {payment_503_index}")

failed_tests = []
for index, (test_name, status, result) in enumerate(
        test_results, 1):
    if result == "passed":
        continue
    elif result == "failed":
        failed_tests.append(f"{index} | {test_name} | {status}")
print(failed_tests)

first_server_error = None
for test_name, status, result in test_results:
    if status >= 500:
        first_server_error = (test_name, status, result)
        break

if first_server_error is not None:
    test_name, *error_info = first_server_error
else:
    test_name, *error_info = (None, None, None)

print(f"first_server_error: {first_server_error}")
print(f"first_server_error_name: {test_name}")
print(f"error_info: {error_info}")
