from email.message import EmailMessage
import ssl
import smtplib
import json
from main import main_menu
cart_file = "purchase/cart.json"
prod_file = "Product/prod.json"
cus_file = "Customer/customer.json"


def purchase_operation():
    while True:
        print("""
        ***** Purchase menu *****
        [1].MAKE PURCHASE
        [2].VIEW ALL PURCHASES
        [0].MAIN MENU
        
        """)
        option = input('Input an option to proceed:')

        if option == "1":

            make_purchase()

        elif option == "2":

            completed_orders()

        elif option == "0":
            main_menu()
        else:
            print('\nINVALID MENU OPTION!')


def make_purchase():
    fin_order = {}
    with open("purchase/cart.json", "r") as json_file:
        order_temp = json.load(json_file)
    if not order_temp:
        from Customer.customer import view_customer
        view_customer()
        with open(cus_file, "r") as json_file:
            cus_temp = json.load(json_file)
            data_lent = len(cus_temp)
            while True:
                try:
                    cust_id = int(input(f"\nEnter Customer ID of the customer:\n"))
                except ValueError:
                    print(f"\nINVALID INPUT!")
                    continue
                if cust_id > data_lent:
                    print("CUSTOMER NOT FOUND!")
                    continue
                else:
                    break

            i = 1
            for entry in cus_temp:
                if i == int(cust_id):
                    fin_order["Customer Name"] = entry["Customer_Name"]
                    fin_order["Email"] = entry["Email"]
                    order_temp.append(fin_order)
                    i = i + 1
                else:
                    pass
                    i = i + 1
        from Product.product import view_product
        view_product()

        with open(prod_file, "r") as json_file:
            prod_temp = json.load(json_file)
        data_length = len(prod_temp)

        with open("purchase/cart.json", "r") as json_file:
            cart_temp = json.load(json_file)
        opt = int(input(f"\nEnter Product ID(1 - {data_length}) of item you wish to add to cart:"))
        i = 1
        for entry in prod_temp:

            if i == int(opt):
                prod_id = create_prod_id()
                fin_order[prod_id] = {}
                prod_qty = entry["Product_Quantity"]
                fin_order[prod_id]["Product_id"] = opt
                fin_order[prod_id]["Product_Name"] = entry["Product_Name"]
                fin_order[prod_id]["Product_Quantity"] = int(input(f"\nEnter quantity (less than or equal "
                                                                   f"to {prod_qty}) you wish to purchase:"))
                fin_order[prod_id]["Product_Price"] = entry["Product_Price"]
                price_tint = float(fin_order[prod_id]["Product_Price"])
                subtt = price_tint * fin_order[prod_id]["Product_Quantity"]
                fin_order[prod_id]["Sub-Total"] = '{:.2f}'.format(subtt)
                cart_temp.append(fin_order)
                i = i + 1

            else:
                pass
                i = i + 1
        with open("purchase/cart.json", "w") as json_file:
            json.dump(cart_temp, json_file, indent=4)
            print("\nITEM AADED TO CART!")

    #checkout
    else:
        from Product.product import view_product
        view_product()
        with open(prod_file, "r") as json_file:
            prod_temp = json.load(json_file)
        data_length = len(prod_temp)

        with open("purchase/cart.json", "r") as json_file:
            cart_temp = json.load(json_file)

        opt = int(input(f"\nEnter Product ID of item to purchase:"))
        i = 1
        for entry in prod_temp:

            if i == int(opt):
                prod_id = create_prod_id()
                fin_order[prod_id] = {}
                prod_qty = entry["Product_Quantity"]
                fin_order[prod_id]["Product_id"] = opt
                fin_order[prod_id]["Product_Name"] = entry["Product_Name"]
                fin_order[prod_id]["Product_Quantity"] = int(input(f"\nEnter quantity (less than or equal "
                                                                   f"to {prod_qty}) you wish to purchase:"))
                fin_order[prod_id]["Product_Price"] = entry["Product_Price"]
                price_tint = float(fin_order[prod_id]["Product_Price"])
                subtt = price_tint * fin_order[prod_id]["Product_Quantity"]
                fin_order[prod_id]["Sub-Total"] = '{:.2f}'.format(subtt)
                [open_cart_temp] = cart_temp
                open_cart_temp.update(fin_order)

                i = i + 1

            else:
                pass
                i = i + 1
        with open("purchase/cart.json", "w") as json_file:
            json.dump(cart_temp, json_file, indent=4)
            print("\nProduct Added to cart!")

    while True:
        cont_shopping = int(input("\nPress 1 to continue shopping and 2 to checkout:"))
        if cont_shopping == 1:
            make_purchase()
        elif cont_shopping == 2:
            # calculating total
            with open("purchase/cart.json", "r") as json_file:
                checkout_temp = json.load(json_file)
            emp_prd = {}
            [opened_checkout_temp] = checkout_temp
            new_id = "Total"
            total = 0
            for i in opened_checkout_temp:
                if i == "Customer Name":
                    continue
                elif i == "Email":
                    continue
                else:
                    subt_tint = float(opened_checkout_temp[i]["Sub-Total"])
                    total += subt_tint
            emp_prd[new_id] = "{:.2f}".format(total)
            opened_checkout_temp.update(emp_prd)

            with open("purchase/cart.json", "w") as json_file:
                json.dump(checkout_temp, json_file, indent=4)
        break

    # receipt
    with open("purchase/cart.json", "r") as json_file:
        fin_temp = json.load(json_file)
    [strip_fin_temp] = fin_temp
    
    print("**************RECEIPT***************")
    for i in strip_fin_temp:
        if i == "Customer Name":
            print(f"\nCustomer Name: {strip_fin_temp[i]}")
        elif i == "Email":
            pass
        elif i == "Total":
            print(f"\nTotal: Ksh. {strip_fin_temp[i]}")
        else:
            print(f"\nProduct Name: {strip_fin_temp[i]['Product_Name']}")
            print(f"Product Quantity: {strip_fin_temp[i]['Product_Quantity']}")
            print(f"Product Price: Ksh. {strip_fin_temp[i]['Product_Price']}")
            print(f"Sub-Total: Ksh. {strip_fin_temp[i]['Sub-Total']}")

    print("-------Thank you for Shopping with us---------")

    send_mail()
    # inventory decreament after purcgase
    with open("purchase/cart.json", "r") as json_file:
        pid_temp = json.load(json_file)
    [open_pid] = pid_temp
    for i in open_pid:
        if i == "Customer Name":
            continue
        elif i == "Email":
            continue
        elif i == "Total":
            continue
        else:
            p_id_list = open_pid[i]["Product_id"]
            p_qty_list = open_pid[i]["Product_Quantity"]
            with open(prod_file, "r") as json_file:
                prod_temp = json.load(json_file)
            up_qty_list = []
            j = 1
            for entry in prod_temp:
                if j == p_id_list:
                    prod_name = entry["Product_Name"]
                    prod_qty = entry["Product_Quantity"]
                    prod_price = entry["Product_Price"]
                    prod_qty = prod_qty - p_qty_list
                    up_qty_list.append({"Product_Name": prod_name,
                                        "Product_Quantity": prod_qty,
                                        "Product_Price": prod_price})
                    j = j + 1
                else:
                    up_qty_list.append(entry)
                    j = j + 1
            with open("Product/prod.json", "w") as json_file:
                json.dump(up_qty_list, json_file, indent=4)

    # generating a purchase list
    with open("purchase/cart.json", "r") as json_file:
        c_temp = json.load(json_file)
    [strip_c_temp] = c_temp
    with open("purchase/purchase.json", "r") as json_file:
        o_temp = json.load(json_file)

    pur_combo = {}
    order_id = create_pur_id()
    pur_combo[order_id] = strip_c_temp
    if not o_temp:
        o_temp.append(pur_combo)
    else:
        [open_o_temp] = o_temp
        open_o_temp.update(pur_combo)

    with open("purchase/purchase.json", "w") as json_file:
        json.dump(o_temp, json_file, indent=4)
        print("\nOrder record captured!")
    # emptying the cart
    cart = []
    with open("purchase/cart.json", "w") as json_file:
        json.dump(cart, json_file, indent=4)

    purchase_operation()


def create_prod_id():
    with open("purchase/cart.json", "r") as json_file:
        gen_temp = json.load(json_file)
    if not gen_temp:
        new_id = "Prod1"
        return new_id
    else:
        [open_gen_temp] = gen_temp
        prev_id = list(open_gen_temp)[-1]
        length = len(prev_id)
        num = int(prev_id[4:length]) + 1
        new_id = "Prod" + str(num)
        return new_id


def create_pur_id():
    with open("purchase/purchase.json", "r") as json_file:
        od_temp = json.load(json_file)
    if not od_temp:
        new_id = "Ord1"
        return new_id
    else:
        [open_od_temp] = od_temp
        prev_id = list(open_od_temp)[-1]
        length = len(prev_id)
        num = int(prev_id[3:length]) + 1
        new_id = "Ord" + str(num)
        return new_id



def completed_orders():
    with open("purchase/purchase.json", "r") as json_file:
        o_temp = json.load(json_file)
    [strip_o_temp] = o_temp

    print("\n************RECENT PURCHASES*****************\n")

    for i in strip_o_temp:
        print(f"Order: {i}")
        for j in strip_o_temp[i]:
            if j == "Customer Name":
                print(f"Customer Name: {strip_o_temp[i]['Customer Name']}")
            elif j == "Email":
                pass
            elif j == "Total":
                print(f"Total: Ksh. {strip_o_temp[i]['Total']}\n")
            else:
                p_name = strip_o_temp[i][j]['Product_Name']
                p_price = strip_o_temp[i][j]['Product_Price']
                p_qty = strip_o_temp[i][j]['Product_Quantity']
                print(f"Product Name: {p_name}, Product Price: {p_price}, "
                      f"Product Quantity: {p_qty}, Sub-Total: Ksh. {strip_o_temp[i][j]['Sub-Total']}")

    print("/n/n")


def send_mail():

    with open("purchase/cart.json", "r") as json_file:
        fin_temp = json.load(json_file)
    [strip_fin_temp] = fin_temp

    email_sender = 'wamahigadev@gmail.com'
    email_pass = "ydupfucuckvvkjpf"
    email_receiver = ''

    subject = "MAMA MBOGA GROCERIES"

    body = "\n"
    body += "***********PURCHASE RECEIPT**************"
    body += "\n"

    for i in strip_fin_temp:
        if i == "Customer Name":
            body += f"\nCustomer Name: {strip_fin_temp[i]}"
        elif i == "Total":
            body += f"\nTotal: Ksh. {strip_fin_temp[i]}"
        elif i == "Email":
            email_receiver = {strip_fin_temp[i]}
        else:
            body += f"\n\nItem: {strip_fin_temp[i]['Product_Name']}"
            body += f"\nQty: {strip_fin_temp[i]['Product_Quantity']}"
            body += f"\nPrice: Ksh. {strip_fin_temp[i]['Product_Price']}"
            body += f"\nTotal: Ksh. {strip_fin_temp[i]['Sub-Total']}"
            body += "\n"
    
    body += "\n\n******THANKYOU FOR SHOPPING WITH US******"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_pass)
        smtp.sendmail(email_sender, email_receiver, em.as_string())



