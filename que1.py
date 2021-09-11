# Q.1 Json data ko python object main convert karne ka program likho?.

# Example:

# Input :-
input={
     "Name":"Ram", 
     "Class":"IV", 
     "Age":9 
     }
# Output :-
# {
#     'Name': 'Ram', 
#     'Class': 'IV', 
#     'Age': 9
# }

import json
input={
     "Name":"Ram", 
     "Class":"IV", 
     "Age":9 
     }
f=json.dumps(input,indent=2)#this is going to convert our python object to a json string
print(type(f))
f=json.loads(f)#now we are going to load this json string into a python object#it only worls on json objects.therefore we have previously converted our python dictionary to json string using the dumps method.
print(f)
print(type(f))
#without dumping
import json
input='''{
     "Name":"Ram", 
     "Class":"IV", 
     "Age":9 
     }'''
#now we are have created a json string without conversion
f=json.loads(input)
print(f)
print(type(f))
