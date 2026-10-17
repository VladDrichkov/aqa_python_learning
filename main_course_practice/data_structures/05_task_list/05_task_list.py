suite_names = ["auth", "payments", "profile"]

test_names = [
    ["login", "logout", "refresh"],
    ["create_payment", "refund"],
    ["get_profile", "update_profile", "delete_profile"],
]

statuses = [
    [200, 500, 200],
    [201, 503],
    [200, 400, 204],
]

problem_tests = []
for index, suite_name in enumerate(suite_names, 1):
    for test_name, status in zip(test_names[index-1], statuses[index-1]):
        if status < 400:
            continue
        problem_tests.append(f"{index} | {suite_name} | {test_name} | {status}")
        # print(index, test_name, status)
print(problem_tests)

# failed_suite_names = [
#         suite_name
#         for index, suite_name in enumerate(suite_names, 0)
#         if [status for status in statuses[index] if status >= 400]
# ]

failed_suite_names = [
        suite_name
        for index, suite_name in enumerate(suite_names, 0)
        if any(status >= 400 for status in statuses[index])
]

print(failed_suite_names)

# for suite, statuses_list in zip(suite_names, statuses):
#     for status in statuses_list:
#         if status >= 400:
#             failed_suite_names.append(suite)
#             break
