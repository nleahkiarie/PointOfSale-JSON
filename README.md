# PointOfSale-JSON
A CLI point of sales

python cli customer of sale
This a command line driven point of sale application that allows a user to make purchases from the stocked inventory.It is a single user interface and all the data is stored in json files

Language used
Python 3

Features
The main menu is the starting point for this application where the user is prompted to choose one of these four modules: 1.Customer operations 2.product operations 3.Purchases 4.search

Customer operations
A user can be able to create a customer,update a customer,delete a customer and also list all the customers in the records.The user can also go back to the main menu.

Product operations
This menu has several sub menus; Create new product,update a product ,delete a product and list all the available products.A user is also given the option to go back to the main menu.

Purchases
The Purchase operations is where the user gets to makes their purchase by searching for customers and products using either their name or id.The system will then check whether the customer and products are available in the records(json files) if not,the user is prompted with an error message.The system will then proceed to check whether the quantity of the product ordered excceds the ones in stock.When the purchase is succesful,they user is prompted to either make another purchase or checkout.At the end,the inventory is updated and a receipt with the purchase details is generated.The receipt is then sent to the customers email

search
In this option a user can search for customer by using their name or their phone number.and search for product using the product name
