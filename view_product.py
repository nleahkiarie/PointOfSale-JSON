import json
filename ="Product/prod.json"


def view_product():
    with open(filename , "r") as f:
        temp = json.load(f)
        i = 1
        for entry in temp:
            prod_name = entry["Product_Name"]
            prod_qty = entry["Product_Quantity"]
            prod_price = entry["Product_Price"]
            print(f"ProductID: {i}")
            print(f"Product name: {prod_name} , Quantity: {prod_qty}, Price: Ksh. {prod_price}")
            i = i + 1

            