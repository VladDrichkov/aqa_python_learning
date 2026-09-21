# response = {
#     "status": 200,
#     "message": "ok"
# }
#
# print([] in response)
#
# response = {
#     "status": 500,
#     "message": "ok",
#     "error": "timeout"
# }
#
# response.update({
#     "status": 500,
#     "error": "timeout"
# })
import copy

keys = ["passed", "failed", "skipped"]
result = {key: [] for key in keys}

print(result)

response = {
    "user": {
        "name": "Alex",
        "roles": ["qa", "admin"]
    }
}
admin = response["user"]["roles"][1]
print(admin)

response = {
    "data": {
        "users": [
            {"name": "Alex", "status": "active"},
            {"name": "Bob", "status": "blocked"}
        ]
    }
}

blocked = response["data"]["users"][1]["status"]
print(blocked)

response.copy()
copy.deepcopy(response)
