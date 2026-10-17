
def build_report(tests):

    failed_tests = [test for test in tests if test["status"] == "failed"]
    failed_tests.sort(
        key= lambda test : (
            -test["retries"], -test["duration_ms"], test["name"])
    )
    return failed_tests


def main():
    tests = [
        {"name": "login", "status": "failed", "retries": 2, "duration_ms": 500},
        {"name": "payment", "status": "failed", "retries": 3, "duration_ms": 700},
        {"name": "cart", "status": "failed", "retries": 3, "duration_ms": 900},
        {"name": "checkout", "status": "failed", "retries": 3, "duration_ms": 900},
        {"name": "profile", "status": "failed", "retries": 2, "duration_ms": 800},
        {"name": "search", "status": "failed", "retries": 1, "duration_ms": 1200},

        {"name": "logout", "status": "passed", "retries": 5, "duration_ms": 1500},
        {"name": "settings", "status": "passed", "retries": 0, "duration_ms": 100},
    ]

    report = build_report(tests)
    for record in report:
        print(record)


if __name__ == '__main__':
    main()
