print("=" * 25) #for decoration

customerNames = ['Rajesh Mehak', 'Chandan Kumar', 'Priya Srinivas', 'Anjali Chauhan', 'Arushi Changia']
customerPins = ['6456', '3325', '1433', '2580', '9779']
customerBalances = [100000, 75000, 200000, 64000, 29000]
deposit = 0
withdrawl = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0

#Continous Loop
while True:
    print("="*20)
    print(" _____Welcome to Ings Bank_____ ")
    print("*"*20)
    print("=<< 1. Open a new account          >>=")
    print("=<< 2. Withdraw Amount             >>=")
    print("=<< 3. Deposit Amount              >>=")
    print("=<< 4. Check Customers and Balance >>=")
    print("=<< 5. Exit/Leave                  >>=")
    print("*" * 20)

    optionNumber = input("Select your option number from the above menu:")
    if optionNumber == "1":
        print("Option number 1 is selected by the customer")
        
        NOC = eval(input("Number of Customers : "))

        i = i + NOC

        if i > 5:
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i = i - NOC
        else:

            while counter_1 <= i:

                name = input("Provide Fullname : ")
                customerNames.append(name)
                pin = str(input("Please provide a pin of your choice"))
                customerPins.append(pin)
                deposit = eval(input("Please provide a value to add in your balance"))
                balance = balance + deposit
                customerBalances.append(balance)
                print("\n Name =", end = " ")
                print(customerNames[counter_2])
                print("Pin = ", end = " ")
                print(customerPins[counter_2])
                print("Balance = ", end = " ")
                print(customerBalances[counter_2], end = " ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\n Your name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("_____New account has been created successfully!!!_____")
                print("\n")
                print("Your name is available on the customers list now : ")
                print(customerNames)
                print("\n")
                print("Note: Please remember the Name and Pin")
                print("=" * 20)

        mainMenu = input("Please press enter key to go back to main menu")
    elif optionNumber == "2":
        j = 0
        print("Option number 2 is selected by the customer")

        while j < 1:
            k = -1
            name = input("Please provide your name : ")
            pin = input("Please provide your safe pin : ")

            while k < len(customerNames) - 1:
                k = k + 1

                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1

                        print("Your Current Balance is : ", end = " ")
                        print(customerBalances[k], end = " ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])

                        withdrawl = eval(input("Provide the value to with draw from your account : "))

                        if withdrawl > balance:

                            deposit = eval(input("Please deposit a higher value because your balance mentioned above is not enough!!!"))

                            balance = balance + deposit
                            print("Your Current Balance : ", end = " ")
                            print(balance, end = " ")
                            print("-/Rs\n")
                            balance = balance - withdrawl
                            print("-\n")
                            print("_____Withdraw Successfull!!!!_____")
                            customerBalances[k] = balance
                            print("Your New Balance is : ", balance, end = " ")
                            print("-/Rs\n\n")
                        else:

                            balance = balance - withdrawl

                            print("\n")
                            print("_____Withdraw Successfull!!!_____")
                            customerBalances[k] = balance
                            print("Your New Balance is : ", balance, end = " ")
                            print("-/Rs\n\n")
            if j < 1:

                print("Your name an pin does not match!!!\n")
                break

        mainMenu = input("Please press enter key to go back to main menu")
    elif optionNumber == "3":
        print("Option number 3 is selected by the customer")
        n = 0

        while n < 1:
            k = -1
            name = input("Please provide your name : ")
            pin = input(" Please provide your safe pin : ")

            while k < len(customerNames) - 1:
                k = k + 1

                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1

                        print("Your Current Balance is : ", end = " ")
                        print(customerBalances[k], end = " ")
                        print("-/Rs")
                        balance = (customerBalances[k])

                        deposit = eval(input("Enter the value you want to deposit in your account : "))
                        balance = balance + deposit
                        customerBalances[k] = balance
                        print("\n")
                        print("_____Deposit Successfull!!!_____")
                        print("Your New Balance is : ", balance, end = " ")
                        print("=/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!!\n")
                break

        mainMenu = input("Please press enter key to go back to main menu")
    elif optionNumber == "4":
        print("Option number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances are mentioned below : ")
        print("\n")

        while k <= len(customerNames) - 1:
            print("=>.Customer = ", customerNames[k])
            print("=>.Balance = ", customerBalances[k], end = " ")
            print("-/Rs")
            print("\n")
            k = k + 1

        mainMenu = input("Please press enter key to go back to main menu")
    elif optionNumber == "5":

        print("Option number 5 is selected by the customer")
        print("Thank you for using our banking system!!")
        print("\n")
        print("Visit us again")
        print("Adios")
        break
    else:

        print("Invalid option selected by the customer")
        print("Please Try Again!!")

        mainMenu = input("Please press enter key to go back to main menu")