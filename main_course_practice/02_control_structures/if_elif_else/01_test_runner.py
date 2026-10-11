
def can_access(role, environment, has_vpn, has_approval, working_hours):
    is_test_enable = role in ("qa", "developer")
    is_stage_enable = role in ("qa", "developer") and has_vpn
    is_prod_enable = (
            (role == "qa" and has_vpn and has_approval and working_hours) or
            (role == "admin" and has_vpn)
    )

    access_allowed = (
            (environment == "prod" and is_prod_enable) or
            (environment == "test" and is_test_enable) or
            (environment == "stage" and is_stage_enable)
    )

    return access_allowed


def run_tests(cases):
    for case in cases:
        actual = can_access(**case["input"])
        expected = case["expected"]

        if actual == expected:
            print(f'PASS: {case["name"]}')
        else:
            print(
                f'FAIL: {case["name"]} | expected={expected}, actual={actual}'
            )


cases = [
    {
        "name": "qa can access test without vpn",
        "input": {
            "role": "qa",
            "environment": "test",
            "has_vpn": False,
            "has_approval": False,
            "working_hours": True,
        },
        "expected": True,
    },
    {
        "name": "developer can access test without vpn",
        "input": {
            "role": "developer",
            "environment": "test",
            "has_vpn": False,
            "has_approval": False,
            "working_hours": True,
        },
        "expected": True,
    },
    {
        "name": "admin cannot access test",
        "input": {
            "role": "admin",
            "environment": "test",
            "has_vpn": True,
            "has_approval": True,
            "working_hours": True,
        },
        "expected": False,
    },
{
    "name": "qa can access stage with vpn",
    "input": {
        "role": "qa",
        "environment": "stage",
        "has_vpn": True,
        "has_approval": False,
        "working_hours": True,
    },
    "expected": True,
},
{
    "name": "qa cannot access stage without vpn",
    "input": {
        "role": "qa",
        "environment": "stage",
        "has_vpn": False,
        "has_approval": False,
        "working_hours": True,
    },
    "expected": False,
},
{
    "name": "developer can access stage with vpn",
    "input": {
        "role": "developer",
        "environment": "stage",
        "has_vpn": True,
        "has_approval": False,
        "working_hours": True,
    },
    "expected": True,
},
{
    "name": "developer cannot access stage without vpn",
    "input": {
        "role": "developer",
        "environment": "stage",
        "has_vpn": False,
        "has_approval": False,
        "working_hours": True,
    },
    "expected": False,
},
{
    "name": "qa can access prod with vpn approval during working hours",
    "input": {
        "role": "qa",
        "environment": "prod",
        "has_vpn": True,
        "has_approval": True,
        "working_hours": True,
    },
    "expected": True,
},
{
    "name": "qa cannot access prod without approval",
    "input": {
        "role": "qa",
        "environment": "prod",
        "has_vpn": True,
        "has_approval": False,
        "working_hours": True,
    },
    "expected": False,
},
{
    "name": "qa cannot access prod without vpn",
    "input": {
        "role": "qa",
        "environment": "prod",
        "has_vpn": False,
        "has_approval": True,
        "working_hours": True,
    },
    "expected": False,
},
{
    "name": "qa cannot access prod outside working hours",
    "input": {
        "role": "qa",
        "environment": "prod",
        "has_vpn": True,
        "has_approval": True,
        "working_hours": False,
    },
    "expected": False,
},
{
    "name": "admin can access prod with vpn during working hours",
    "input": {
        "role": "admin",
        "environment": "prod",
        "has_vpn": True,
        "has_approval": False,
        "working_hours": True,
    },
    "expected": True,
},
{
    "name": "admin can access prod with vpn outside working hours",
    "input": {
        "role": "admin",
        "environment": "prod",
        "has_vpn": True,
        "has_approval": False,
        "working_hours": False,
    },
    "expected": True,
},
{
    "name": "admin cannot access prod without vpn",
    "input": {
        "role": "admin",
        "environment": "prod",
        "has_vpn": False,
        "has_approval": False,
        "working_hours": False,
    },
    "expected": False,
},
{
    "name": "developer cannot access prod",
    "input": {
        "role": "developer",
        "environment": "prod",
        "has_vpn": True,
        "has_approval": True,
        "working_hours": True,
    },
    "expected": False,
},
{
    "name": "unknown environment is denied",
    "input": {
        "role": "qa",
        "environment": "dev",
        "has_vpn": True,
        "has_approval": True,
        "working_hours": True,
    },
    "expected": False,
},
]

run_tests(cases)

