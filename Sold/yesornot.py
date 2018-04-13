
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

def update_data():

    file = open('magazyn.csv', 'r+')
    d = input("Do you want update a data? Press y or n!")

    if d == "y":
        for line in file:
            product_for_delete = input("Enter product? ")
            find_product(product_for_delete)




    elif d == "n":
        print("Thank You for using my magazin :) ")




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