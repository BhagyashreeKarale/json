import json
driver_details='''{"driver1":{"name":"Name : Shyam",
          "contact no.":"Contact : 9847673643",
          "rating":"Rating : 4.3/5",
          "location":"",
          "vehicle_no":"Number Plate : MH 12 RK 5668"},
"driver2":{"name":"Name : Dayanand",
          "contact no.":"Contact : 9573264683",
          "rating":"Rating : 4.3/5",
          "location":"",
          "vehicle_no":"Number Plate : MH 12 SS 4674"},

"driver3":{"name":"Name : Hari",
          "contact no.":"Contact : 9798357934",
          "rating":"Rating : 4.0/5",
          "location":"",
          "vehicle_no":"Number Plate : MH 12 SD 6587"},
"driver4":{"name":"Name : Rakesh",
          "contact no.":"Contact : 9847736434",
          "rating":"Rating : 4.5/5",
          "location":"",
          "vehicle_no":"Number Plate : MH 12 WE 7682"},
"driver5":{"name":"Name : Nayak",
          "contact no.":"Contact : 9476736434",
          "rating":"Rating : 3.9/5",
          "location":"",
          "vehicle_no":"Number Plate : MH 12 IP 8762"}
        }'''
near_by='''{"Swargate":["7lovers point","Bhasker petrol pump","Aranyashwar","Panchami hotel","Parvati"],
"Katraj":["Bharti Vidyapith","Raja Rani baugh","Rajesh society","Katraj chowk","Balaji nagar"],
"Khopi":["Flora institute","Khed Shivapur Toll Plaza","Bapdeo ghat","Katraj ghat","Shri Bhairavnath mandir"],
"Upper":["Bibwewadi","Dhankawadi","Shivtejnagar","Kondhwa","Indiranagar"]}'''
feedback='''{"driver1":"","driver1":"","driver2":"","driver3":"","driver4":"","driver5":""}'''
income='''{"driver1":0,"driver1":0,"driver2":0,"driver3":0,"driver4":0,"driver5":0}'''
pdata=json.loads(driver_details)
pdata_nearby=json.loads(near_by)
pickup_point=input("Enter your current location:\n")
drop_point=input("Enter your destination:\n")
from random import sample
for nearbypoint in pdata_nearby:
    if pickup_point==nearbypoint:
        range_forloop=len(pdata_nearby[nearbypoint])
        for drivers in range(range_forloop):
            pdata["driver"+str(int(drivers+1))]["location"]="Driver's location : "+pdata_nearby[nearbypoint][drivers]+", 3 km away from your current location." 
print("\nOla partners nearby your location are:\n")
no=0
for keys in pdata:
    no=no+1
    print("Driver"+str(no))
    for key2 in pdata[keys]:
        print(pdata[keys][key2])
    print()
driver_choice=int(input("Enter option number of the chosen driver:\n"))
if driver_choice >= 1 and driver_choice<=5 :
    letters = sample('0123456789', 4)
    if letters[0] == '0':
        letters.reverse()
    otp =int(''.join(letters))
    print("Your OTP : ",otp)
    otpinput=int(input("Please enter the OTP provided:\n"))
    if otp == otpinput:
        print("Verification successful!")
        amount=int(input("Enter total amount according to 5rs/km:\n"))
        payment_method=int(input("For online payment enter 1:\nFor cash payment enter 2:\n"))
        if payment_method == 1:
            payment_done=input("UPI no.=7686987908\nOnce payment is done,enter 'done':\n")
            if payment_done=="done":
                print("Booking confirmed:)\nThe driver will reach out super soon!\nWish you happy and safe journey:)")
                income=json.loads(income)
                income["driver"+str(driver_choice)]+=amount
            else:
                print("The ride will begin after payment")
        else:
            cash=input("Enter 'done' when cash payment is done:\n")
            if cash == "done":
                print("Booking confirmed:)\nThe driver will reach out super soon!\nWish you happy and safe journey:)")
                income=json.loads(income)
                income["driver"+str(driver_choice)]+=amount
                
            else:
                print("The ride will begin after payment")
    else:
        print("Incorrect OTP")
else:
    print("Incorrect option number")
     