def main():
    # response = {
    #     "status": 200,
    #     "request_id": "req-481"
    # }
    # # response = {}
    # if not response:
    #     result = {}
    # else:
    #     result = response["request_id"]
    #
    # result = response and response["request_id"]
    # print (result)

    # test_result = {
    #     "status": "failed",
    #     "error": "TimeoutError"
    # }
    # test_result = None
    #
    #
    # if test_result and isinstance(test_result, dict):
    #     error_msg = test_result["error"]
    # else:
    #     error_msg = {}
    #
    # error_msg = test_result and test_result["error"]
    #
    # print(error_msg)

    # test_result = {
    #     "status": "failed",
    #     "error": "TimeoutError"
    # }
    #
    # # error_msg = None
    # # if isinstance(test_result, dict):
    # #     error_msg = test_result.get("error", None)
    #
    # test_result = None
    # #
    # # или
    # # test_result = "failed"
    #
    # # или
    # # test_result = {}
    # #
    # # # или
    # # test_result = {
    # #     "status": "failed"
    # # }
    #
    # # или
    # # test_result = {
    # #     "status": "failed",
    # #     "error": "TimeoutError"
    # # }
    # #
    #
    # error_msg = (test_result is not None
    #              and not isinstance(test_result, str)
    #              and test_result.get("error")
    #              or None
    #              )
    # #
    # print(error_msg)
    #
    # configured_url = ""
    # default_url = "https://test.example.com"
    #
    # if not configured_url:
    #     base_url = default_url
    # else:
    #     base_url = configured_url
    #
    # base_url = configured_url or default_url
    # print(base_url)
    #
    # configured_retries = 0
    # default_retries = 3
    #
    # # configured_retries = None
    #
    # if configured_retries is None:
    #     retry_count = default_retries
    # else:
    #     retry_count = configured_retries
    #
    # retry_count = default_retries if configured_retries is None else configured_retries
    #
    # retry_count = configured_retries is None and default_retries or configured_retries

    # print(retry_count)

     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    tests = [
        {"name": "login", "status": 200},
        {"name": "profile", "status": 201},
        {"name": "payment", "status": 500},
        {"name": "logout", "status": 204},
    ]

    has_server_error = any((test["status"] >= 500 for test in tests))
    print(has_server_error)

    tests = [
        {"name": "login", "status": 200},
        {"name": "profile", "status": 201},
        {"name": "logout", "status": 204},
    ]

    all_successful = all(200 <= test["status"] < 300 for test in tests)
    print(all_successful)

    tests = []

    for test in tests:
        print(test["status"])

        
    all_successful = any([
        200 <= test["status"] < 300
        for test in tests
    ])

    print(all_successful)


if __name__ == '__main__':
    main()
