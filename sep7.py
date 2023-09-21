def withdraw():
    print("enter your withdraw amount:")

    var=input("do you want to continiue type yes, otherwise type no:")
    if var=="yes":
        main_function()
    else:
        print("thanks for visiting IOB ATM")

def balance():
    print("you balance is 2500")
    var=input("do you want to continiue type yes, otherwise type no:")
    if var=="yes":
        main_function()
    else:
        print("thanks for visiting IOB ATM")

def statment():
    print("your statment is generatte3d")
    var=input("do you want to continiue type yes, otherwise type no:")
    if var=="yes":
        main_function()
    else:
        print("thanks for visiting IOB ATM")

def deposit():
    print("your 300 amount is deposited successfully")
    var=input("do you want to continiue type yes, otherwise type no:")
    if var=="yes":
        main_function()
    else:
        print("thanks for visiting IOB ATM")


def main_function():

    print("****IOB ATM***")
    print("press 1->withdraw")
    print("press 2->balance")
    print("press 3->statmnet")
    print("press 4->deposit")

    user=int(input("enter your number:"))

    if user==1:
        withdraw()
        
    elif user==2:
        balance()
       
    elif user==3:
        statment()
      
    elif user==4:
        deposit()
       
    else:
        print("pls type 1234 only")

main_function()


