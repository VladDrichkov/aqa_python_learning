run_1_failed = {
    "test_login",
    "test_payment",
    "test_profile",
    "test_search",
}

run_2_failed = {
    "test_payment",
    "test_orders",
    "test_search",
    "test_refund",
}

ever_failed_tests = run_1_failed.union(run_2_failed)
failed_in_both_runs = run_1_failed.intersection(run_2_failed)
failed_only_in_first_run = run_1_failed.difference(run_2_failed)
tests_failed_in_exactly_one_run = run_1_failed.symmetric_difference(run_2_failed)
first_run_failures_are_subset = run_1_failed.issubset(ever_failed_tests)
all_failures_include_second_run_failures = ever_failed_tests.issuperset(run_2_failed)

print(ever_failed_tests)
print(failed_in_both_runs)
print(failed_only_in_first_run)
print(tests_failed_in_exactly_one_run)
print(first_run_failures_are_subset)
print(all_failures_include_second_run_failures)

