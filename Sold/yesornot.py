

def menu():
    print("""
        1 - Enter product
        2 - Find product
        3 - Delete product
        4 - Exit
    """)
    choice = input("Chose element from menu and press Enter: ")
    if choice == "1":
        print("\nHello, you can add new products!  \n")
        enter_product()
    elif choice == "2":
        print("\nHello, you can add find products!  \n")
        find_product("What are you looking for? ")
    elif choice == "3":
        print("\nHello, you can update data!  \n")
        delete_product()
    elif choice == "4":
        print("\n Goodbay!")

def back_menu(p):

    back = input(p)
    if back == "0":
        menu()
    else:
        print("Wrong answer!")


def enter_product():
    """
    Enter name and amount of product.
    All product will sign up into file magazyn.csv as list.

    """
    n = int(input('How many product do you enter? '))          #n is the number of items you want to enter
    db =[]
    for i in range(n):
        a = input("Enter the name of product and amount: ")
        #kasia 2
        a = a.replace(" ", ",") # zamiana  stargo na nowe
        a += "\n"
        #kasia, 2
        db.append(a)

    with open ("magazyn.csv","a") as file:
        file.writelines(db)

    back_menu("Thank you for adding new products. Press 0 and back to menu. \n")


def find_product(p):
    """
    Enter the name product which you are looking for.
    Then you get back information how many products are in magazine.

    """
    import re

    s = input(p)
    file = open('magazyn.csv', 'r')

    for line in file:
        if re.match(s,line):
            print(f"I found: ", line)
            break
    else:
        print(f"I can't find {s} in magazyn.csv")
        query_yes_no('Do you want add more?')

    back_menu("Great! \n")

def delete_product() -> object:
    import re

    db = []

    file_read = open('magazyn.csv', 'r+')

    product_to_delete = input('Enter product wjich will be delete: ')

    for line in file_read:
        re.search(product_to_delete, line)
        b = product_to_delete.replace(product_to_delete, " " )
        db.append(b)

    with open ("magazyn.csv","r+") as file:
        file.writelines(db)

    # back_menu("Thank you. Press 0 and back to menu. \n")

def query_yes_no(q) -> object:
    while True:
        question = input(q + "Press: (y/n)" + "\n")
        if question == "y":
            enter_product()
        elif question == "n":
            print("All data is saving in magazyn.csv file")
            break
        else:
            print("Please enter y or n, only.")