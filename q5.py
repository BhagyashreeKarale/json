
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# write code to print the value of salary
pobj=json.loads(sampleJson)    
print(pobj['company']['employee']['payble']['salary'])
# print(pobj['company']['employee']['payble'].get('salary'))#this is using the get function


