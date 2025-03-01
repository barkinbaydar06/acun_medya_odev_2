def modeSelection():
    print("\nPlease enter the mode you want to run.\n'P' for prime number detector.\n'C' for calculator.")
    print("You can change the mode by entering 'M' inside each mode")
    print("Enter 'Q' to terminate.")
    
    choice = input("\nMode choice: ").strip().upper()
    
    if choice == 'P':
        print("\nWelcome to prime detector")
        print("---------------------------")
        while True:
            num = input("Please enter a number: ")
            if num.isdigit():
                num = int(num)
                break
            else:
                print("Error! Please enter a valid integer.")

        primeMode(num)

    elif choice == 'C':
        print("Welcome to calculator")
        print("---------------------------")
        calcMode()
        

    elif choice == 'Q':
        print("\nExiting program...")
        exit()

    else:
        print("Invalid choice. Please enter 'P', 'C', or 'Q'.")
        modeSelection()


def primeMode(param):
    while True:
        if param == 'M' or param == 'm':
            modeSelection()
            return

        try:
            param = int(param)
        except ValueError:
            print("Error! Please enter a valid integer.")
            param = input("Enter new number ('M' for Mode Change): ")
            continue

        isPrime = True

        if param < 2:
            isPrime = False
        else:
            for i in range(2, param // 2 + 1):
                if param % i == 0:
                    isPrime = False
                    break

        if isPrime:
            print("This number is a prime number!")
        else:
            print("This number is not prime!")

        param = input("Enter new number ('M' for Mode Change): ")
        
def calcMode():
    while True:
        while True:
            num1 = input("\nPlease enter the first number: ")
            try:
                num1 = int(num1)
                break
            except ValueError:
                print("Error! Please enter a valid integer.")

        while True:
            num2 = input("Please enter the second number: ")
            try:
                num2 = int(num2)
                break
            except ValueError:
                print("Error! Please enter a valid integer.")

        while True:
            oper = input("Please enter the operation (+, -, *, /): ")
            if oper in ('/', '*', '+', '-'):
                break
            else:
                print("Invalid operation. Please enter one of: /, *, -, +")

        if oper == '/' and num2 == 0:
            print("Error: Cannot divide by zero.")
            print("Returning to the beginning of the calculator...\n")
            continue

        if oper == '/':
            print("The result is:", num1 / num2)
        elif oper == '*':
            print("The result is:", num1 * num2)
        elif oper == '-':
            print("The result is:", num1 - num2)
        elif oper == '+':
            print("The result is:", num1 + num2)

        print("\nEnter M to change mode.\nQ to terminate.\nAnything else to continue in calculator.\n")
        choiceCalc = input("Enter choice: ").strip().upper()

        if choiceCalc == 'M':
            modeSelection() 
            return  
        elif choiceCalc == 'Q':
            print("Ending the program...")
            exit()

modeSelection()
