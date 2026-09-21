# report_data = {
#     "test_name": "test_create_user",
#     "status": 500,
#     "duration": 1.42,
#     "raw_response": '{"error": "database unavailable"}',
# }
#
# applied_overrides = {
#     "timeout": 10,
#     "retries": 3,
#     "base_url": "https://staging-api.example.com",
# }
#
# raw_response = report_data.pop("raw_response")
# override_name, override_value = applied_overrides.popitem()
#
# print(f"report_data: {report_data}")
# print(f"raw_response: {raw_response}")
# print(f"applied_overrides: {applied_overrides}")
# print(f"override_name: {override_name}")
# print(f"override_value: {override_value}")
#
# response = {
#     "status": 200,
#     "data": {"user_id": 42},
#     "debug_info": None,
# }

response = {
    "status": 200,
    "data": {"user_id": 42},
}

MISSING = object()

debug_info_was_present = "debug_info" in response
debug_info = response.pop("debug_info", MISSING)

print(f"response: {response}")
print(f"debug_info: {debug_info}")
print(f"debug_info_was_present: {debug_info_was_present}")

