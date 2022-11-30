import time
import datetime

#global list (variable)
order = [0,0,0,0]
sales_tax = .055
total = 0
#order column 0 is small col 1 is med col 2 is large col 3 is xl

#definitions of functions
def main():
    global order, sales_tax, total
    while True:
        add_pizza()
        option = str(input("Do you want another pizza?(yes/no)"))
        if option == "n" or option == "no" or option == "No":
            break
    recipit()



def add_pizza():
    global order
    za = str(input("What size pizza would you like? Small, Med, Lg, XL?"))
    if za == "small" or za == "s" or za == "Small" or za == "sm" or za == "SMall":
        count = int(input("How many you want?:   "))
        order[0] = order[0] + count 
    #col 0 is small
    elif za == "Med" or za == "med" or za == "M" or za == "m" or za == "Medium" or za == "medium":
        count = int(input("How many of this size would you like?:   "))
        order[1] = order[1] + count  
    #col 1 is med
    elif za == "large" or za == "lg" or za == "Large" or za == "LG" or za == "LARGE" or za == "lARGE":
        count = int(input("How many of this size would you like?:   "))
        order[2] = order[2] + count  
    #col 2 is large
    elif za == "x" or za == "X" or za == "XL" or za == "xl" or za == "Extra Large" or za == "extra large":
        count = int(input("How many of this size would you like?:   "))
        order[3] = order[3] + count  
    #col 3 is xl
    else: 
        print("Incorrect input. This selection was not added to your order... You are being returned to pizza menu prior to this interaction.")
        time.sleep(3)

def recipit():
    global order, sales_tax, total
    smallTotal = 9.99 * order[0]
    mediumTotal = 12.99 * order[1]
    largeTotal = 14.99 * order[2]
    xlargeTotal = 17.99 * order[3]
    sales_tax = (smallTotal + mediumTotal + largeTotal + xlargeTotal) * .055
    total = smallTotal + mediumTotal + largeTotal + xlargeTotal + sales_tax
    print('-------------------------------')
    print('********PALERMO PIZZA********')
    print('Your neighborhood pizza joint')
    print('-------------------------------')
    print('Small        $ ' + format(smallTotal,'8,.2f'))
    print('Med          $ ' + format(mediumTotal,'8,.2f'))
    print('Large        $ ' + format(largeTotal,'8,.2f'))
    print('XLarge       $ ' + format(xlargeTotal,'8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax,'8,.2f'))
    print('Total        $ ' + format(total,'8,.2f'))
    print('-------------------------------')
    print(str(datetime.datetime.now()))
    print("Thank you for your business!")


main()
    
