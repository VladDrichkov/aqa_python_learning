# results = [
#     ("test_login", 200, 0.34),
#     ("test_profile", 503, 1.42),
#     ("test_checkout", 404, 0.81),
#     ("test_search", 502, 1.15),
#     ("test_logout", 200, 0.27),
# ]
#
# server_errors = []
# slow_tests = []
# first_server_error = None
#
# for test_name, status, duration in results:
#     if 500 <= status < 600:
#         server_error = test_name, duration
#         server_errors.append(server_error)
#         if first_server_error is None:
#             first_server_error = (test_name, status, duration)
#     if duration > 1.0:
#         slow_tests.append(test_name)
#
# print(server_errors)
# print(slow_tests)
# print(first_server_error)
#
# attempts = [
#     ("test_payment", 503, 1),
#     ("test_payment", 502, 2),
#     ("test_payment", 200, 3),
# ]
# failed_attempts = []
# successful_attempt = None
# last_failed_status = None
#
# for test_name, status, attempt_number in attempts:
#     if status >= 500:
#         failed_attempt = test_name, status, attempt_number
#         failed_attempts.append(failed_attempt)
#         last_failed_status = status
#     elif status == 200:
#         successful_attempt = test_name, status, attempt_number
#         break
#
# print(failed_attempts)
# print(successful_attempt)
# print(last_failed_status)
#
#
# test_data = (
#     "test_login",
#     ["smoke", "api"],
#     200,
# )
#
# test_data[1].append("critical")
# print(test_data)

test_runs = [
    {
        "suite": "auth",
        "results": [
            ("test_login", 503, 1.20, ["api", "critical"]),
            ("test_login", 200, 0.42, ["api", "critical"]),
            ("test_logout", 200, 0.31, ["api"]),
        ],
    },
    {
        "suite": "profile",
        "results": [
            ("test_get_profile", 404, 0.55, ["api"]),
            ("test_update_profile", 502, 1.75, ["api", "slow"]),
            ("test_update_profile", 503, 1.61, ["api", "slow"]),
            ("test_update_profile", 200, 0.90, ["api", "slow"]),
        ],
    },
    {
        "suite": "payments",
        "results": [
            ("test_create_payment", 500, 2.10, ["api", "critical"]),
            ("test_create_payment", 502, 1.95, ["api", "critical"]),
            ("test_refund", 200, 0.80, ["api"]),
        ],
    },
]

recovered_test = []
unrecovered_test = []
slow_server_errors = []

for run in test_runs:
    temp_results_name_500 = {}
    for result_name, result_status, result_duration, other in run["results"]:
        if 500 <= result_status < 600:
            temp_results_name_500.update({result_name: result_status})

            if result_duration > 1.5:
                temp_full_slow_tuple = result_name, result_status, result_duration, other
                slow_server_errors.append(temp_full_slow_tuple)

        elif result_status == 200 and result_name in temp_results_name_500:
            temp_result = run["suite"], result_name, temp_results_name_500[result_name], result_status
            recovered_test.append(temp_result)
            temp_results_name_500.pop(result_name)

    for test_name, test_status in temp_results_name_500.items():
        tmp_unrecovered_tuple = run["suite"], test_name, test_status
        unrecovered_test.append(tmp_unrecovered_tuple)

report = {
    "recovered_test": recovered_test,
    "unrecovered_test": unrecovered_test,
    "slow_server_errors": slow_server_errors
}

print()
for k,v in report.items():
    print(k)
    print(v)
