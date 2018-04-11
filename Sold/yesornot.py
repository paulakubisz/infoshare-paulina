

def enter_product():
    """
    Enter name and amount of product.
    All product will sign up into file magazyn.csv as list.

    """
    n = int(input('How many item do you enter? '))          #n is the number of items you want to enter
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



def query_yes_no(question, default="n"):
    """


    """
    while True:
        from pip._vendor.distlib.compat import raw_input
        question = raw_input("Are you finish?" "Press: (y/n)" + "\n")
        if question == "n":
            enter_product()
        elif question == "y":
            print("All data is saving in magazyn.csv file")
            break
        else:
            print("Please enter y or n, only.")