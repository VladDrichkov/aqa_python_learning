
from functools import cmp_to_key

def compare(a,b):
    if a[1] != b[1]:
        if a[1] == "failed":
            return -1
        else:
            return 1
    # else:
    #     if a[2] == b[2] and a[0] < b[0]:
    #         return -1
    #     elif a[2] == b[2] and a[0] > b[0]:
    #         return 1
    #     elif a[2] != b[2] and a[2] > b[2]:
    #         return -1
    #     elif a[2] != b[2] and a[2] < b[2]:
    #         return 1
    else:
        if a[2] == b[2]:
            if a[0] < b[0]:
                return -1
            elif a[0] > b[0]:
                return 1
        elif a[2] > b[2]:
            return -1
        elif a[2] < b[2]:
            return 1
    return 0

results = [
    ("profile", "passed", 120),
    ("payment", "failed", 450),
    ("login", "failed", 300),
    ("logout", "passed", 80),
    ("cart", "failed", 450),
    ("payment", "failed", 450),
]

results = sorted(results, key=cmp_to_key(compare))

for result in results:
    print(result)

