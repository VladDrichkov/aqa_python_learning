failed_tests = [
    "test_login",
    "test_payment",
    "test_profile",
    "test_payment",
    "test_logout",
]

failed_tests.append("test_search")
failed_tests.extend(["test_cart", "test_orders"])
failed_tests.insert(1, "test_auth")
failed_tests.remove("test_payment")
deleted = failed_tests.pop()
test_payment_count = failed_tests.count("test_payment")
test_payment_index = failed_tests.index("test_payment")
failed_tests.sort()

print(failed_tests)
print(deleted)
print(test_payment_count)
print(test_payment_index)
