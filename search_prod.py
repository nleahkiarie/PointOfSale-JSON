import json
filename = "./Product/prod.json"

def product_search():
    while True:
        print("""
               *********PRODUCT SEARCH MENU *******
               [1]. SEARCH BY NAME
               [0]. BACK
                 """)
        option = input('Enter an option to proceed:')
        if option == "1":
            search_name()
        elif option == "0":
            from search.search import search
            search()
        else:
            print('INVALID MENU OPTION!')

# search for a product by name
def search_name():
    while True:
        prod_name = input("\nEnter name of product to search:")
        check = check_prod(prod_name)
        if check == 'y':
            break
        else:
            print("\nPRODUCT NOT FOUND!")


def check_prod(prod_name):
    with open(filename , "r") as json_file:
        c_prod_temp = json.load(json_file)
    for entry in c_prod_temp:
        if prod_name in entry['Product_Name']:
            print(f"Product Name: {entry['Product_Name']}")
            print(f"Product Quantity: {entry['Product_Quantity']}")
            print(f"Product Price: {entry['Product_Price']}")
            return 'y'
        else:
            continue
    return