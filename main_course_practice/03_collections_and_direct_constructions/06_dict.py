run_data = {
    "environment": "staging",
    "metadata": {
        "build": "2026.09.10-42",
        "branch": "feature/profile",
        "debug": "temporary-data",
    },
    "suites": [
        {
            "name": "auth",
            "owner": "team-auth",
            "tests": [
                {
                    "name": "test_login",
                    "status": "passed",
                    "http_status": 200,
                    "duration": 0.42,
                    "tags": ("smoke", "api"),
                },
                {
                    "name": "test_refresh",
                    "status": "failed",
                    "http_status": 503,
                    "duration": 1.72,
                    "tags": ("api", "critical"),
                    "error": "upstream unavailable",
                },
                {
                    "name": "test_logout",
                    "status": "skipped",
                    "http_status": None,
                    "duration": 0,
                    "tags": (),
                },
            ],
        },
        {
            "name": "profile",
            "owner": "team-profile",
            "tests": [
                {
                    "name": "test_get_profile",
                    "status": "passed",
                    "http_status": 200,
                    "duration": 0.61,
                    "tags": ("api",),
                },
                {
                    "name": "test_update_profile",
                    "status": "failed",
                    "http_status": 500,
                    "duration": 2.15,
                    "tags": ("api", "critical", "slow"),
                    "error": None,
                },
                {
                    "name": "test_delete_profile",
                    "status": "",
                    "http_status": None,
                    "duration": 0,
                    "tags": ("experimental",),
                },
            ],
        },
    ],
}

meta = run_data["metadata"].copy()
meta.pop("debug", None)
meta.update({"environment": run_data["environment"], "suites": len(run_data["suites"])})

status_count = {}
failed_by_suite = {}
error_statuses = set()
slow_failures = []
failure_tags = set()
owners_with_failures = set()

for suite in run_data["suites"]:
    for test in suite["tests"]:
        if test["status"]:
            count = status_count.setdefault(test["status"], 0) + 1
            status_count[test["status"]]  = count

            if test["status"] == "failed":
                tmp_list = failed_by_suite.setdefault(suite["name"], [])
                tmp_list.append(test["name"])

                if 400 <= test["http_status"] < 600: error_statuses.add(test["http_status"] )

                for tag in test["tags"]:
                    failure_tags.add(tag)
                owners_with_failures.add(suite["owner"])
                if test["duration"] > 1.5:
                    tmp = suite["name"], test["name"], test["duration"]
                    slow_failures.append(tmp)


report = {
    "meta": meta,
    "status_counts": status_count,
    "failed_by_suite": failed_by_suite,
    "error_statuses": error_statuses,
    "slow_failures": slow_failures,
    "failure_tags": failure_tags,
    "owners_with_failures": owners_with_failures,
}

for k,v in report.items():
    print(k)
    print(v)
    print()

print(run_data["metadata"])

# print(status_count)
# print(failed_by_suite)
# print(error_statuses)
# print(slow_failures)
# print(failure_tags)
# print(owners_with_failures)
#

# for item in items:
#     ...
#     if condition:
#         break
# else:
#     ...



