# Python object ko json data main convert karne ka program likho?

# Input :-
# {
#      "name": "David",
#      "class":"I",
#      "age": 6  
#  }
# Output:-

# {
#     "name": "David", 
#     "class": "I", 
#     "age": 6
# }
import json
Input={
     "name": "David",
     "class":"I",
     "age": 6  
      }

jsdata=json.dumps(Input)#you can directly print it without storing it in a variable
print(jsdata)
