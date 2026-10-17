run_1 = {"login", "payment", "profile", "search"}
run_2 = {"payment", "orders", "search", "refund"}

critical_tests = {"payment", "refund", "checkout"}

changed_tests = run_1.symmetric_difference(run_2)
print(changed_tests)
critical_changed_tests = changed_tests.intersection(critical_tests)
print(critical_changed_tests)
has_critical_failures = not (run_1.union(run_2)).isdisjoint(critical_tests)
print(has_critical_failures)