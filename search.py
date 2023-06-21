from search.search_prod import product_search
from search.search_cus import customer_search


def search():
    while True:
        print("""
        **************SEARCH MENU******************
                [1].SEARCH CUSTOMER
                [2].SEARCH PRODUCT
                [0].EXIT
        """)

        option = input('Input an option to proceed:')

        if option == "1":
             customer_search()
             break
        elif option == "2":
            product_search()
            break
        elif option == "0":
            print("\nBack to main menu!")
            from main import main_menu
            main_menu()
        else:
            print('\nINVALID OPTION! please try again')

