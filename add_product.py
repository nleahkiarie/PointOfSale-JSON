import json
from Product.view_product import view_product 
from main import main_menu
filename = "Product/prod.json"

def add_product():
    view_product
    prod_data = {}
    with open(filename, "r") as f:
        temp = json.load(f)

    prod_data["Product_Name"] = input("\nEnter product's name: ")

    while True:
        try:
            prod_data["Product_Quantity"] = int(input("\nEnter quantity: "))
        except ValueError:
            print(f"\nINVALID INPUT!")
            continue
        break
    while True:
        try:
            price = int(input("\nEnter price: "))
        except ValueError:
            print(f"\nINVALID INPUT!")
            continue
        prod_data["Product_Price"] = '{:.2f}'.format(price)
        break
    temp.append(prod_data)
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
        print("\nProduct Added successfully!")
        print("*******************************")
        main_menu