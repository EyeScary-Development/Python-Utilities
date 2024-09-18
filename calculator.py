command = input("Would you like to go home? \n y/n").

while command == "y":
    Operation = input("Operations are \n Addition (Type 1) \n Subtraction (Type 2) \n Division (Type 3) \n Multiplication (Type 4) \n Square Num 1 (Type 5) \n Cube Num1 (Type 6) \n Power of 4 (Type 7) \n So which operation do you want to use?: ")
    Num1 = int(input("What is the first number you want to use this operation with: "))
    Num2 = int(input("What is the second number you want to use this operation with: "))
    if Operation == "1":
        print(Num1," + ",Num2," = ",Num1 + Num2)
    elif Operation == "2":
        print(Num1," - ",Num2," = ",Num1 - Num2)
    elif Operation == "3":
        print(Num1," / ",Num2," = ",Num1 / Num2)
    elif Operation == "4":
        print(Num1," * ",Num2," = ",Num1 * Num2)
    elif Operation == "5":
        print(Num1," squared is ",Num1 * Num1)
    elif Operation == "6":
        print(Num1," cubed is ",Num1*(Num1*Num1))
    elif Operation == "7":
        print(Num1," to the power of 4 is ",(Num1*(Num1*Num1))*Num1)
    else:
        print("Not Valid")
    
    command=input("would you like to go home? y/n: ")

import main

