while True:
    print("1. Add")
    print("2. Minus")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice =="1":

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 + num2

        print("Result is: ",result)
    
    elif choice == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 - num2

        print("Result is: ",result)
    elif choice == "3":
        print("Program End")

        break
    