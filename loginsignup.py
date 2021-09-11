import json
import os.path
def checkexisting_id(id):
    with open("/home/bhagyashri/Desktop/JSON/practice/1.json","r") as file:
        data=file.read()
        data1=json.loads(data)
        for i in data1:
            if i["username"] == id:
                return True
        return False
def dumping(data):
    with open ("/home/bhagyashri/Desktop/JSON/practice/1.json","w" ) as file:
        json.dump(data,file,indent=2)
def checkexisting_pwd(pwdinput):
    with open("/home/bhagyashri/Desktop/JSON/practice/1.json","r") as file:
        data=file.read()
        data1=json.loads(data)
        for i in data1:
            if i["password"] == pwdinput:
                return True
        return False
logORsignup = input("Enter 1 for login \nEnter 2 for signup \n")
if logORsignup == "1" :
    idinput = input ("Enter username :\n")
    file_exists = os.path.exists('/home/bhagyashri/Desktop/JSON/practice/1.json')
    if file_exists==True:
        if checkexisting_id(idinput)==False:
            print("ID doesn't exist!\nCreate a new one.")
        else:
            pwdinput=input("Enter password :\n")
            if checkexisting_pwd(pwdinput) == True:
                print("Login successfull.")
            else:
                print("Incorrect password")
    else:
        print("ID doesn't exist!")         
elif logORsignup == "2" :
    account={}
    id = input ("Enter username :\n")
    file_exists = os.path.exists('/home/bhagyashri/Desktop/JSON/practice/1.json')
    if file_exists==True:
        if checkexisting_id(id) == True:
            print("Id already exists.\nPlease login")
        else:
            pwd = input ("Enter a strong password :\n")
            account["username"]=id
            account["password"]=pwd
            with open("/home/bhagyashri/Desktop/JSON/practice/1.json","r") as file:
                data=file.read()
                data1=json.loads(data)
                data1.append(account)
                dumping(data1)
    else:
        pwd=input("Enter password:\n")
        account["username"]=id
        account["password"]=pwd
        dumping([account])
        

            
                


   

