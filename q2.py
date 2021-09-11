import json
sampleJson = """{"key1": "value1", "key2": "value2"}"""
# write code to print the value of key2


#answer:
pobject=json.loads(sampleJson)
print(pobject["key2"])
