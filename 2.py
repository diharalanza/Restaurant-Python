name = input("Hello, what is your name?: ")

maple= 3.50
strawberry= 2.25
vanilla= 4.05
honey= 1.99

count1 = 0
count2 = 0
count3 = 0
count4 = 0

stop = False

def CalcPrice():
    price= (count1*3.5 + count2*2.25 + count3*4.05 + count4*1.99)
    return price

while stop == False:



    choice = input("""What would you like:
    1. Chocolate-dipped Maple Puff ($3.50 each)
    2. Strawberry Twizzler ($2.25 each)
    3. Vanilla Chai Strudel ($4.05 each)
    4. Honey-drizzled Lemon Dutchie ($1.99)
    5. No more doughnuts.\n\n""")

    if (choice != "1" and choice != "2" and choice != "3" and choice != "4"):
        if choice == "5":
            print(name + ", here is your receipt: ")
            if count1 != 0:
                print(str(count1) + " Chocolate-dipped Maple Puffs")

            if count2 != 0:
                print(str(count2) + " Strawberry Twizzlers")

            if count3 != 0:
                print(str(count3) + " Vanilla Chai Strudels")

            if count4 != 0:
                print(str(count4) + " Honey-drizzled Lemons")

            print("Total Price: $" + str(CalcPrice()))
            print("Thank you, have a nice day!")

            stop = True

        else:
            print("I'm sorry, that's not a valid selection. Please enter a selection from 1-4.\n\n")



    else:

        stop1 = True
        while stop1 == True:


            quan = input("how many would you like?: ")
            if quan.isdigit():




                stop1 = False
                if choice==str(1):
                    count1 = count1 + 1
                    variety= "Chocolate-dipped Maple Puff"

                elif choice==str(2):
                    count2 = count2 + 2
                    variety= "Strawberry Twizzler"

                elif choice==str(3):
                    count3 = count3 + 3
                    variety= "Vanilla Chai Strudel"

                elif choice==str(4):
                    count4 = count4 + 4
                    variety= "Honey-drizzled Lemon Dutchie"

                elif choice==str(5):
                    variety=0
                    stop = True
            else:

                print("I'm sorry, that's not a valid selection. Please enter a selection from 1-4.")
