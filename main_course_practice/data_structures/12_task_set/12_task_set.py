all_tests = {
    "login",
    "payment",
    "profile",
    "search",
    "orders",
    "refund",
}

failed_tests = {
    "payment",
    "orders",
    "refund",
}

critical_tests = {
    "payment",
    "login",
    "refund",
}

critical_failures = set()
regular_failures = set()

for test in all_tests:
    if test not in failed_tests:
        continue
    elif test in critical_tests:
        critical_failures.add(test)
    else:
        regular_failures.add(test)

print(critical_failures)
print(regular_failures)

is_valid_critical_group = (
    critical_failures.issubset(critical_tests)
)
print(is_valid_critical_group)

