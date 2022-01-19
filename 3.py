name = input("""\n\nWelcome, to Dino's International Doughnut Shoppe!
Please enter your name to begin: """)

maple= 3.50
strawberry= 2.25
vanilla= 4.05
honey= 1.99

count1 = 0
count2 = 0
count3 = 0
count4 = 0

stop = False

def CalcPrice(currency):
    price= (count1*3.5 + count2*2.25 + count3*4.05 + count4*1.99)

    if currency == str(1):
         price = "$" + str(price) + " (CAD)"

    elif currency == str(2):
        price = str(price*0.66) + " (EUR)"

    elif currency == str(3):
        price = "$" + str(price*0.77) + " (USD)"

    return price

while stop == False:



    choice = input("""\nWhat would you like:\n
    1. Chocolate-dipped Maple Puff ($3.50 each)
    2. Strawberry Twizzler ($2.25 each)
    3. Vanilla Chai Strudel ($4.05 each)
    4. Honey-drizzled Lemon Dutchie ($1.99)
    5. No more doughnuts.\n\n""")

    if (choice != "1" and choice != "2" and choice != "3" and choice != "4"):
        if choice == "5":
            stop3 = False
            while stop3 == False:


                cur = input("""What currency will you be paying with?:\n
                1. CAD
                2. EUR
                3. USD\n\n""")

                if (cur != "1" and cur != "2" and cur != "3"):
                    print("\nInvalid selection. Please select one of the three options\n")
                else:
                    stop3 = True

            print("\n" + name + ", here is your receipt: \n")
            if count1 != 0:
                print(str(count1) + " Chocolate-dipped Maple Puffs")

            if count2 != 0:
                print(str(count2) + " Strawberry Twizzlers")

            if count3 != 0:
                print(str(count3) + " Vanilla Chai Strudels")

            if count4 != 0:
                print(str(count4) + " Honey-drizzled Lemons")

            print("\nTotal Price: " + str(CalcPrice(cur)))
            print("\nThank you, have a nice day!")

            stop = True

        else:
            print("\nI'm sorry, that's not a valid selection. Please enter a selection from 1-4.")



    else:

        stop1 = True
        while stop1 == True:


            quan = input("\nhow many would you like?:\n\n")
            if quan.isdigit():




                stop1 = False
                if choice==str(1):
                    count1 = count1 + 1


                elif choice==str(2):
                    count2 = count2 + 2


                elif choice==str(3):
                    count3 = count3 + 3


                elif choice==str(4):
                    count4 = count4 + 4


                elif choice==str(5):
                    variety=0
                    stop = True
            else:

                print("\nI'm sorry, that's not a valid selection. Please enter a selection from 1-4.")
