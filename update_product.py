from fileinput import filename
import json
from Product.view_product import view_product
from main import main_menu
filename = "Product/prod.json"

def update_product():
    view_product()
    new_data= []
    with open(filename, "r") as json_file:
        temp = json.load(json_file)
        data_length = len(temp)
        while True:
            try:
                update_opt = int(input(f"\nEnter Product ID of the product to update:"))
            except ValueError:
                print(f"\nINVALID PRODUCT ID ")
                continue
            if update_opt > data_length:
                print(f"\nPRODUCT NOT FOUND, ENTER AN ID BETWEEN 1 AND {data_length}")
                continue
            else:
                break
        i = 1
        for entry in temp:
            if i == int(update_opt):
                prod_name = entry["Product_Name"]
                prod_price = entry["Product_Price"]
                prod_qty = entry["Product_Quantity"]
                print(f" Current Product name: {prod_name}")
                prod_name = input("Enter new product name: ")
                print(f" Current  Product Quantity: {prod_qty}")
                while True:
                    try:
                        prod_qty = int(input("\nEnter new product quantity: "))
                    except ValueError:
                        print(f"\nINVALID INPUT!")
                        continue
                    break
                print(f"Price: Ksh. {prod_price}")
                while True:
                    try:
                        new_price = int(input("\nEnter new product price: "))
                    except ValueError:
                        print(f"\nINVALID INPUT!")
                        continue
                    prod_price = '{:.2f}'.format(new_price)
                    break
                new_data.append({"Product_Name": prod_name,
                                          "Product_Quantity": prod_qty,
                                          "Product_Price": prod_price})
                i = i + 1

            else:
                new_data.append(entry)
                i = i + 1

    with open(filename, "w") as json_file:
        json.dump(new_data, json_file, indent=4)
        print("******************************")
        print("\nPRODUCT UPDATED SUCCESSFULY!!")
        print("******************************")

        main_menu()

