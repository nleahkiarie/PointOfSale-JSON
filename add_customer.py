import json
import re
from main import main_menu
filename ="Customer/customer.json"

def add_customer():
    cus_data = {}

    with open(filename, "r") as json_file:
        temp = json.load(json_file)

    cus_data["Customer_Name"] = input("\nEnter customer's name: ")
    while True:
        try:
            gender_rec = int(input("\nSelect 1 if customer is Male and 2 if customer is Female: "))
        except ValueError:
            print(f"\nINVALID INPUT!")
            continue
        if gender_rec == 1:
            cus_data["Gender"] = "Male"
            break
        elif gender_rec == 2:
            cus_data["Gender"] = "Female"
            break
        else:
            print("\nINVALID INPUT! Please enter 1 or 2!")
    while True:
        mail = input("\nEnter customer's email:")
        confirm_format = checky(mail)
        if confirm_format == 'y':
            cus_data["Email"] = mail
            break
        else:
            print("\nINVALID EMAIL FORMAT! ")
            continue

    while True:
        ftel_in = input("\nEnter customer's phone number:  ")
        confirm_pformat = check_numformat(ftel_in)
        if confirm_pformat == 'y':
            cus_data["Phone_Number"] = ftel_in
            break
        else:
            print("\nINVALID PHONE NUMBER FORMAT!")
            continue

    temp.append(cus_data)
    with open(filename , "w") as json_file:
        json.dump(temp, json_file, indent=4)
        print("\nCustomer Added successfully!")
        main_menu()


# Email format validation
def checky(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return 'y'
    else:
        return


# number format validation
def check_numformat(telno):
    regex = r'^[01 | 07]{2}[0-9]{8}$'
    if re.fullmatch(regex, telno):
        return 'y'
    else:
        return