# Problems: Printing prices are based on the number of copies to be printed
# This program prompts the user for the number of copies to print and then displays the price per copy and the total price for the job

def inputNumber():
    while True:
        try:
            num = int(input("Please enter the number of copies to print: "))
        except ValueError:
            print("Not an integer! Try again!!")
            continue
        else:
            return num
            break

def printN(num):
    if (num > 1000):
        ppc = 0.25
    elif (num <= 1000 and num >= 750):
        ppc = 0.26
    elif (num >= 500 and num <= 749):
        ppc = 0.27
    elif (num >= 100 and num <= 499):
        ppc = 0.28
    else:
        ppc = 0.30
    print("Price per copy is: $", ppc)
    print("Total cost is: $", ppc * num)

repeat = True
while (repeat == True):
    num = inputNumber()
    printN(num)
    while True:
        re = input("Would you like to enter another number? (Y/N): ")
        if (re == "N" or  re == "n"):
            repeat = False
            break
        elif (re == "Y" or re == "y"):
            break
        else:
            print("That's not Y or N! Try again!!")
            continue
