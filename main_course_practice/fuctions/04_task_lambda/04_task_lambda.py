
def build_report(tests):
    result = [test for test in tests if test["status"] == "failed"]
    result.sort(
        key=lambda test: (-test["duration_ms"], test["name"])
    )
    result = [f"{record["name"]}: {record["duration_ms"]}" for record in result]
    return result

def main():
    tests = [
        {"name": "login", "status": "failed", "duration_ms": 420},
        {"name": "profile", "status": "passed", "duration_ms": 180},
        {"name": "payment", "status": "failed", "duration_ms": 730},
        {"name": "logout", "status": "passed", "duration_ms": 95},
        {"name": "cart", "status": "failed", "duration_ms": 420},
    ]

    report = build_report(tests)
    for record in report:
        print(record)


if __name__ == '__main__':
    main()


