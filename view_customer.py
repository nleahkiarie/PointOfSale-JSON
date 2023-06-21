import json
filename = "./Customer/customer.json"

def view_customer():
    with open(filename, "r") as json_file:
        temp = json.load(json_file)
        i = 1
        for entry in temp:
            cus_name = entry["Customer_Name"]
            gender = entry["Gender"]
            mail = entry["Email"]
            tel = entry["Phone_Number"]
            print(f"CustomerID: {i}")
            print(f"Name: {cus_name}, Gender: {gender}, Email: {mail}, Phone number: {tel}")
            i = i + 1


    
          

            