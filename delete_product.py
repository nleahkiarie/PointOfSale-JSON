import json
from Product.view_product import view_product
from main import main_menu

filename = "Product/prod.json"

def delete_product():
    view_product()
    del_data = []
    with open(filename, "r") as f:
        temp = json.load(f)
        if not temp:
            print("INVENTORY IS EMPTY!")
        else:
            data_length = len(temp)
            while True:
                try:
                    delete_opt = int(input(f"\nEnter Product ID to delete:"))
                except ValueError:
                    print(f"\nINVALID INPUT")
                    continue
                if delete_opt > data_length:
                    print(f"\nPRODUCT NOT FOUND! Enter product Id between 1 and {data_length}")
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
        with open(filename, "w") as f:
            json.dump(del_data, f, indent=4)
            print("\nPRODUCT DELETED SUCCESSFULLY!!")
