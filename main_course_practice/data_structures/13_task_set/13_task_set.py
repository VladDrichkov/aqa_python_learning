all_tests = {
    "login",
    "payment",
    "profile",
    "search",
    "orders",
    "refund",
    "logout",
}

failed_tests = {
    "payment",
    "orders",
    "refund",
    "search",
}

critical_tests = {
    "payment",
    "refund",
    "login",
}

blocked_tests = {
    "refund",
    "logout",
}

retry_tests = failed_tests - blocked_tests
print(retry_tests)
critical_retry_tests = retry_tests.intersection(critical_tests)
print(critical_retry_tests)

retry_report = []
for test in retry_tests:
    if test in critical_tests:
        retry_report.append(f"{test} | CRITICAL")
    else:
        retry_report.append((f"{test} | REGULAR"))

critical_but_not_failed = critical_tests - failed_tests
print(critical_but_not_failed)

