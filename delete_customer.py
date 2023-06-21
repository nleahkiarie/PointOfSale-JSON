from fileinput import filename
import json
from Customer.view_customer import view_customer
filename = "Customer/customer.json"

def delete_customer():
    view_customer()
    del_data = []
    with open(filename, "r") as json_file:
        temp = json.load(json_file)
        data_length = len(temp)
        while True:
            try:
                delete_opt = int(input(f"\nEnter Customer ID to delete:"))
            except ValueError:
                print(f"\nInvalid input! customer Id has to be a number")
                continue
            if delete_opt > data_length:
                print(f"\nCustomer not found! Enter an  ID number between 1 and {data_length}")
                continue
            else:
                break

        i = 1
        for entry in temp:
            if i == int(delete_opt):
                pass
                i = i + 1
            else:
                del_data.append(entry)
                i = i + 1

    with open(filename, "w") as json_file:
        json.dump(del_data, json_file, indent=4)
        print("\nCustomer deleted successfully!")
