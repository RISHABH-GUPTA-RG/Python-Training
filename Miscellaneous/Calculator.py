import os
import shutil
import time

os.system("title CALCULATOR MADE BY RISHABH GUPTA")

def clear():
    os.system('cls')

def t():
    time.sleep(1)
    
cols, rows =shutil.get_terminal_size()
try:

    while True:
        print(("CALCULATOR ").center(cols))
        print()
        print(("Made by RISHABH GUPTA").center(cols))
        print()
        print()
        print("SELECT THE OPERATION YOU WANT TO PERFORM")
        print()
        print("SELECT a FOR ADDITION")
        print()
        print("SELECT b FOR SUBSTRACTION")
        print()
        print("SELECT c FOR MULTIPLICATION")
        print()
        print("SELECT d FOR DIVISION")
        print()
        print("PRESS Ctrl+C TO EXIT")
        print()

        choice = input("Enter choice(a/b/c/d):->> ")
        print()
        if choice in ('a', 'b', 'c', 'd', 'A', 'B', 'C', 'D'):
            num1 = float(input("Enter first number:->> "))
            print()
            num2 = float(input("Enter second number:->> "))

            if choice == 'a':
                print("ADDITION OF ", num1, " and ", num2, " is ", num1+num2)
     
            elif choice == 'b':
                print("SUBSTRACTION OF ", num1, " from ", num2, " is ", num2-num1)

            elif choice == 'c':
                print("MULTIPLICTION OF", num1, " and ", num2, " is ", num1*num2)

            elif choice == 'd':
                print("DIVISION OF", num1, " from ", num2, " is ", num1/num2)

            if choice == 'A':
                print("ADDITION OF ", num1, " and ", num2, " is ", num1+num2)
     
            elif choice == 'B':
                print("SUBSTRACTION OF ", num1, " from ", num2, " is ", num2-num1)

            elif choice == 'C':
                print("MULTIPLICTION OF", num1, " and ", num2, " is ", num1*num2)

            elif choice == 'D':
                print("DIVISION OF", num1, " from ", num2, " is ", num1/num2)
                
            print()
            x=input("DO YOU WANT TO CONTINUE(YES/NO)->> ")
            print()
            if x in ('yes','no','YES','NO'):
                 if x=='yes':
                     print(("AS YOUR WISH").center(cols))
                     t()
                     clear()
                     print()
                    
                 elif x=='YES':
                     print(("AS YOUR WISH").center(cols))
                     t()
                     clear()
                     print()
                       
                    
                 elif x=="no":
                     print(("OK, BYE").center(cols))
                     input()
                     t()
                     break
                      
                    
                 elif x=="NO":
                     print(("OK, BYE").center(cols))
                     input()
                     t()
                     break
                          
            else:
                print("Invalid input")
                t()
                clear()
                print()
               
        else:
            print("Invalid Input")
            t()
            clear()
            print()

except KeyboardInterrupt:
    print('\n')
    
