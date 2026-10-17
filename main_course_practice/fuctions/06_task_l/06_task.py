def is_problematic(test):
    if (
        test["status"] == "failed" and
        test["retries"] > 0 and
        test["duration_ms"] >= 400
    ):
        return True
    return False


def main():
    tests = [
        {"name": "login", "status": "failed", "retries": 2, "duration_ms": 450},
        {"name": "payment", "status": "failed", "retries": 0, "duration_ms": 900},
        {"name": "profile", "status": "passed", "retries": 0, "duration_ms": 180},
        {"name": "cart", "status": "failed", "retries": 3, "duration_ms": 300},
    ]

    result = [is_problematic(test) for test in tests]
    print(result)

if __name__ == '__main__':
    main()
