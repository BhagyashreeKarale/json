# Apki pass ek shopping name ki ek dictionary hai

# {
#     "shopping_list":
#         { 
#             "choco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }
# Apki dictionary ka use kar ke ek json file create karna hai. 
# Aur apko kuch task perform karne hai jaise ki

# main dekhna chahta hu shopping list ko json file dekhna.

# phir main user se poochu ga ki kon sa item khareedna chahte ho.

# uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.

# phir aapka wo number of items json file se remove karna hai.

# Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.

# Output:-
import json
shopping_list={
    "shopping_list":{ 
        "choco":"15",
        "Biscuits":"50",
        "Diary_milk":"30",
        "ice_cream":"20",
         } 
}
with open ("myjsonfile.json","w") as pfile:
    json.dump(shopping_list,pfile)
item=input("Enter item name:\n")
unit=int(input("Enter no. of items:\n"))
with open("myjsonfile.json") as f:
    data=json.load(f)
for keys in data:
    if type(data[keys])==dict:
        for item2 in data[keys]:
            if item == item2:
                data[keys][item]=int(data[keys][item])-unit
with open("myjsonfile.json", "w") as jsonFile:
    json.dump(data, jsonFile)


