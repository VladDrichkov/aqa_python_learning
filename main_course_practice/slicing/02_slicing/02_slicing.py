
def filter_items(tests):
    return tests[::-2]

def select_items_reversed(tests, start, stop, step):
    return tests[start:stop:step]

def select_items(tests, start, stop, step):
    return tests[start:stop:step]

def main():
    test_results_1 = [
        "login",
        "profile",
        "payment",
        "logout",
        "search",
        "cart",
        "checkout",
        "notifications",
        "settings",
    ]
    print(filter_items(test_results_1))

    test_results_2 = [
        "login",
        "profile",
        "payment",
        "logout",
        "search",
        "cart",
        "checkout",
        "notifications",
        "settings",
        "security",
    ]
    print(select_items_reversed(test_results_2, -1, -8, -2))

    test_results_3 = [
        "login",
        "profile",
        "payment",
        "logout",
        "search",
        "cart",
        "checkout",
        "notifications",
        "settings",
        "security",
        "billing",
    ]

    print(select_items_reversed(test_results_3, -1, -10, -2))

    test_results_4 = [
        "setup",
        "login",
        "profile",
        "payment",
        "search",
        "cart",
        "checkout",
        "logout",
        "cleanup",
        "report",
        "archive",
    ]

    print(select_items(test_results_4, 2, 9, 2))

    test_results_5 = [
        "setup",
        "login",
        "profile",
        "payment",
        "search",
        "cart",
        "checkout",
        "logout",
        "cleanup",
        "report",
        "archive",
        "metrics",
        "notify",
        "teardown",
    ]

    print(select_items(test_results_5, -2, -13, -2))

if __name__ == '__main__':
    main()
