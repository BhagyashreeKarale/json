# Exercise 1: Convert the following dictionary into JSON format
data = {"key1" : "value1", "key2" : "value2"}


#answer:
import json
data = {"key1" : "value1", "key2" : "value2"}
jsonformat=json.dumps(data)
print(jsonformat)




