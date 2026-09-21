from json.decoder import NaN
from operator import index


def main():

    # failed_tests = [
    #     "test_login",
    #     "test_profile",
    # ]
    #
    # new_failed_test = "test_checkout"
    #
    # operation_result = failed_tests.append(new_failed_test)
    #
    # print(failed_tests)
    # print(operation_result)

    # tests = [
    #     "test_login",
    #     "test_profile",
    # ]
    #
    # new_tests = [
    #     "test_checkout",
    #     "test_logout",
    #     "test_search",
    # ]
    #
    # operation_result = tests.extend(new_tests)
    # print(operation_result)
    # print(tests)
    #
    # retries = [
    #     "retry_1",
    #     "retry_2",
    #     "retry_3",
    #     "retry_4",
    # ]
    #
    # last_retry = retries.pop()
    # print(last_retry)
    # print(retries)

    # failed_tests = [
    #     "test_login",
    #     "test_profile",
    #     "test_checkout",
    #     "test_profile",
    # ]
    #
    # operation_result = failed_tests.remove("")
    # print(operation_result)
    # print(failed_tests)

    # results = [
    #     "passed",
    #     "failed",
    #     "skipped",
    #     "failed",
    # ]
    #
    # removed_status = results.pop(1)
    # print(removed_status)
    # # print(results)
    #
    # statuses = [
    #     "passed",
    #     "failed",
    #     "skipped",
    #     "failed",
    #     "passed",
    #     "failed",
    # ]
    #
    # first_failed_index = statuses.index("failed")
    # failed_count = statuses.count("failed")
    #
    # print(first_failed_index)
    # print(failed_count)
    #
    # durations = [420, 150, 890, 300, 150]
    # sorted_durations = sorted(durations)
    # print(durations)
    # print(sorted_durations)

    # durations = [420, 150, 890, 300, 150]
    # operation_result = durations.sort()
    # print(durations)
    # print(operation_result)

    # statuses = [
    #     "passed",
    #     "failed",
    #     "skipped",
    #     "blocked",
    # ]
    #
    # operation_result = statuses.reverse()
    # print(operation_result)
    # print(statuses)

    # tests = [
    #     "test_login",
    #     "test_profile",
    #     "test_checkout",
    # ]
    #
    # tests_copy = tests.copy()
    # tests.append("test_logout")
    # print(tests_copy)
    # print(tests)

    # steps = [
    #     "create_user",
    #     "delete_user",
    # ]
    #
    # operation_result = steps.insert(1, "get_user")
    # print(steps)
    #
    # results = [
    #     "passed",
    #     "failed",
    #     "skipped",
    #     "failed",
    # ]
    #
    # operation_result = results.clear()
    # print(operation_result)
    # print(results)
    #
    # tests = [
    #     "test_login",
    #     "test_profile",
    #     "test_checkout",
    #     "test_search",
    #     "test_logout",
    #     "test_delete_user",
    # ]
    #
    # first_three = tests[0:3]
    # last_two = tests[-2::1]
    # every_second = tests[::2]
    # reversed_tests = tests[::-1]
    # print(reversed_tests)
    #
    # tests = [
    #     "test_login",
    #     "test_profile",
    #     "test_checkout",
    #     "test_search",
    #     "test_logout",
    #     "test_delete_user",
    #     "test_permissions",
    # ]
    #
    # middle_tests = tests[2:5]
    # without_first_last = tests[1:-1]
    # last_three_reversed = tests[-1:-4:-1]
    # print(middle_tests)
    # print(without_first_last)
    # print(last_three_reversed)
    #
    # failed_tests = [
    #     "test_login",
    #     "test_profile",
    #     "test_checkout",
    #     "test_profile",
    # ]
    #
    # has_profile_failure = "test_profile" in failed_tests
    # search_not_failed = "test_search" not in failed_tests
    # failed_count = len(failed_tests)
    # print(has_profile_failure)
    # print(search_not_failed)
    # print(failed_count)

    # tests = [
    #     "test_login",
    #     "test_profile",
    #     "test_checkout",
    # ]
    #
    # index_of = tests.index("test_checkout")
    # tests.insert(index_of,"test_search")
    # print(tests)

    # tests = [
    #     "test_login",
    #     "test_profile",
    # ]
    #
    # backup = tests
    # tests.append("test_checkout")
    # print(backup)
    #
    # retries = [
    #     "test_login",
    #     "test_profile",
    #     "test_checkout",
    #     "test_search",
    #     "test_logout",
    # ]
    # priority_test = "test_checkout"
    # original_index = None
    # if priority_test in retries:
    #     original_index = retries.index(priority_test)
    #     retries.pop(original_index)
    #     retries.insert(0, priority_test)
    #
    # print(original_index)
    # print(retries)
    #
    # retry_results = [
    #     "passed",
    #     "failed",
    #     "failed",
    #     "passed",
    #     "failed",
    #     "skipped",
    # ]
    #
    # failed_indexes = []
    # non_failed_results = []
    #
    # for i, status in enumerate(retry_results):
    #     if status == "failed":
    #         failed_indexes.append(i)
    #     else:
    #         non_failed_results.append(status)
    #
    # print(failed_indexes)
    # print(non_failed_results)

    test_results = [
        "passed",
        "failed",
        "skipped",
        "failed",
        "passed",
        "failed",
    ]

    # failed_indexes = []
    # for i, status in enumerate(test_results):
    #     if status == "failed":
    #         failed_indexes.append(i)
    # first_failed_index = failed_indexes[0]
    #
    # before_first_failure = test_results[:first_failed_index]

    # failed_indexes = []
    # before_first_failure = []
    # first_failed_index = None
    #
    # for i, status in enumerate(test_results):
    #     if first_failed_index is None and status != "failed":
    #         before_first_failure.append(status)
    #     elif status == "failed":
    #         failed_indexes.append(i)
    #         if first_failed_index is None:
    #             first_failed_index = i
    #
    # print(first_failed_index)
    # print(failed_indexes)
    # print(before_first_failure)

    # responses = [
    #     None,
    #     503,
    #     502,
    #     200,
    #     500,
    # ]
    #
    # success_index = None
    # server_errors = []
    #
    # for index, status in enumerate(responses):
    #     if status is None:
    #         continue
    #     if 500 <= status < 600:
    #         server_errors.append(status)
    #     if status == 200:
    #         success_index = index
    #         break
    #
    # print(success_index)
    # print(server_errors)

    results = [
        {"name": "login", "status": None},
        {"name": "profile", "status": 404},
        {"name": "checkout", "status": 503},
        {"name": "search", "status": 502},
        {"name": "logout", "status": 200},
        {"name": "delete_user", "status": 500},
    ]

    server_error_names = []
    ignored_count = 0
    success_test = None

    for result in results:
        if result["status"] is None or 400 <= result["status"] < 500:
            ignored_count += 1
            # continue
        elif 500 <= result["status"] <= 599:
            server_error_names.append(result["name"])
        elif result["status"] == 200:
            success_test = result["name"]
            break




if __name__ == '__main__':
    main()



