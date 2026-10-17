TEST_NAME = 0
STATUS = 1
DURATION = 2

test_names = ["login", "payment", "profile", "search", "orders", "logout"]
statuses = [200, 503, 200, 404, 500, 200]
durations_ms = [180, 920, 410, 250, 780, 150]

tests = list(zip(test_names, statuses, durations_ms))

problem_tests = [f"{test[TEST_NAME]} | status={test[STATUS]} | duration={test[DURATION]}"
                for test in tests
                if (test[STATUS] >= 400 or test[DURATION] > 600)]
print(problem_tests)

first_server_error = None
for test in tests:
    if test[STATUS] >= 500:
        first_server_error = test[TEST_NAME]
        break
print(first_server_error)

fast_successful_tests = [test[TEST_NAME] for test in tests
                  if test[STATUS] < 400
                  if test[DURATION] <= 400]
print(fast_successful_tests)
