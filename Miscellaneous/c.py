print("SELECT OPERATION.")
print()
print("1 FOR ADDITION")
print()
print("2 FOR SUBSTRACTION")
print()
print("3 FOR MULTIPLICATION")
print()
print("4 FOR DIVISION")
print()
print("PRESS CTRL+C TO EXIT")
try:
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        print()
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            print()
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("ADDITION OF ", num1, " and ", num2, " is ", num1+num2)
    
            elif choice == '2':
                print("SUBSTRACTION OF ", num1, " from ", num2, " is ", num2-num1)

            elif choice == '3':
                print("MULTIPLICTION OF", num1, " and ", num2, " is ", num1*num2)

            elif choice == '4':
                print("DIVISION OF", num1, " and ", num2, " is ", num1/num2)
                
            print()
            x=input("DO YOU WANT TO CONTINUE(y/n)")
            print()
            if x in ('y','n','Y','N'):
                if x=='y':
                    print("AS YOUR WISH")
                elif x=="n":
                    print("OK, BYE")
                    break
                if x=='Y':
                    print("AS YOUR WISH")
                elif x=="N":
                    print("OK, BYE")
                    break
            else:
                print("Invalid input")
                break
        else:
            print("Invalid Input")
except KeyboardInterrupt:
    print('\n')