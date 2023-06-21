import json
from Customer.customer import customer_operations
filename = "./Customer/customer.json"

def customer_search():
    while True:
        print("""
               *********CUSTOMER SEARCH MENU *******
               [1]. SEARCH BY NAME
               [2]. SEARCH BY PHONE NUMBER
               [0]. BACK
                 """)
        option = input('Enter an option to proceed:')
        if option == "1":
            search_name()
            break
        elif option == "2":
            search_phone()
            break
        elif option == "0":
            from search.search import search
            search()
            break
        else:
            print('INVALID MENU OPTION! Enter 1-3')


# search for customer by name
def search_name():
    while True:
        customer_name = input("\nEnter name of customer to search:")
        check = check_name(customer_name)
        if check == 'y':
            break
        else:
            print("CUSTOMER NOT FOUND!")
            break


def check_name(cust_name):
    with open(filename, "r") as json_file:
        customer_temp = json.load(json_file)
    for entry in customer_temp:
        if cust_name in entry['Customer_Name']:
            print(f"Customer Name: {entry['Customer_Name']}")
            print(f"Gender: {entry['Gender']}")
            print(f"Email: {entry['Email']}")
            print(f"Phone Nuumber: {entry['Phone_Number']}")
            return 'y'
        else:
            continue
    return


# search for customer by phone number
def search_phone():
    while True:
        tel = input("\nEnter customer's Phone Number to search:")
        check = check_phone(tel)
        if check == 'y':
            break
        else:
            print("\nCustomer not found! Please input an existing Customer's Phone Number")


def check_phone(cust_phone):
    with open(filename, "r") as json_file:
        customer_temp = json.load(json_file)
    for entry in customer_temp:
        tel = entry['Phone_Number']
        tel= str(tel)
        if cust_phone in tel:
            print(f"Customer Name: {entry['Customer_Name']}")
            print(f"Gender: {entry['Gender']}")
            print(f"Email: {entry['Email']}")
            print(f"Phone Nuumber: {entry['Phone_Number']}")
            return 'y'
        else:
            continue
    return