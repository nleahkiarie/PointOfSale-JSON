from Customer.add_customer import add_customer
from Customer.update_customer import update_customer
from Customer.view_customer import view_customer
from Customer.delete_customer import delete_customer
from main import main_menu

def customer_operations():
    while True:
        print("""
        ******CUSTOMER MENU*********
        [1]. ADD CUSTOMER
        [2]. VIEW CUSTOMERS
        [3]. UPDATE CUSTOMER
        [4]. DELETE CUSTOMER
        [0]. MAIN MENU
        """)
        option = input('Enter an option to proceed:')

        if option == "1":
            add_customer()
            break
        elif option == "2":
            view_customer()
            break
        elif option == "3":
            update_customer()
            break
        elif option == "4":
            delete_customer()
            break
        elif option == "0":
            print("\nBack to main menu!")
            main_menu()
        else:
            print('INVALID OPTION, PLEASE TRY AGAIN!')






