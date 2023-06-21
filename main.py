def main_menu():

    while True:
        print("""
        *****WELCOME TO MAMA MBOGA GROCERIES*****
        **************MAIN MENU******************
                [1].CUSTOMER OPERATIONS
                [2].PRODUCT OPERATIONS
                [3].PURCHASE MENU
                [4].SEARCH
                [0].EXIT
        """)

        option = input('Input an option to proceed:')

        if option == "1":
             from Customer.customer import customer_operations
             customer_operations()
             break

        elif option == "2":

            from Product.product import product_info

            product_info()

            break

        elif option == "3":
            from purchase.purchase import purchase_operation
            purchase_operation()
            break
        elif option == "4":
            from search.search import search
            search()
            break
        elif option == "0":
            exit()
        else:
            print('\nINVALID OPTION! please try again')
            main_menu()


if __name__ == '__main__':
 main_menu()
