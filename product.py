import json
from main import main_menu
from Product.add_product import add_product
from Product.view_product import view_product
from Product.delete_product import delete_product
from Product.update_product import update_product

def product_info():
    while True:

        print("""
        ******* PRODUCT MENU ********
        [1]. ADD PRODUCT
        [2]. LIST PRODUCTS
        [3]. UPDATE PRODUCT
        [4]. DELETE PRODUCT
        [0]. MAIN MENU

        """)
        option = input('Enter an option to proceed:')

        if option == "1":
            add_product()
            break
        elif option == "2":
            view_product()
            break
        elif option == "3":
            update_product()
            break
        elif option == "4":
            delete_product()
            break
        elif option == "0":
            main_menu()
        else:
            print('\nINVALID OPTION, PLEASE TRY AGAIN')




