name = input("Hello, what is your name?: ")

maple= 3.50
strawberry= 2.25
vanilla= 4.05
honey= 1.99

stop = False
while stop == False:

    choice = input("""What would you like:
    1. Chocolate-dipped Maple Puff ($3.50 each)
    2. Strawberry Twizzler ($2.25 each)
    3. Vanilla Chai Strudel ($4.05 each)
    4. Honey-drizzled Lemon Dutchie ($1.99)\n\n""")


    if (choice != "1" and choice != "2" and choice != "3" and choice != "4"):
        print("I'm sorry, that's not a valid selection. Please enter a selection from 1-4.\n\n")



    else:
        stop = True
        stop1 = True
        while stop1 == True:


            quan = input("how many would you like?: ")
            if quan.isdigit():




                stop1 = False
                if choice==str(1):
                    price=int(quan)*maple
                    variety= "Chocolate-dipped Maple Puff"

                elif choice==str(2):
                    price=int(quan)*strawberry
                    variety= "Strawberry Twizzler"

                elif choice==str(3):
                    price=int(quan)*vanilla
                    variety= "Vanilla Chai Strudel"

                elif choice==str(4):
                    price=int(quan)*honey
                    variety= "Honey-drizzled Lemon Dutchie"

                print(name + ", here is your receipt: " + str(quan) + " " + str(variety) + "s. Total Cost: $" + str(price))

            else:

                print("I'm sorry, that's not a valid selection. Please enter a selection from 1-4.")
