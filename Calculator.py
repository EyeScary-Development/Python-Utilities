Operation = input("Which operation do you want to complete \n Addition (Type 1) \n Subtraction (Type 2) \n Division (Type 3) \n Multiplication (Type 4) ")
Num1 = int(input("What is the first number you want to use this operation with"))
Num2 = int(input("What is the second number you want to use this operation with"))
if Operation == "1":
    print(Num1," + ",Num2," = ",Num1 + Num2)
elif Operation == "2":
    print(Num1," - ",Num2," = ",Num1 - Num2)
elif Operation == "3":
    print(Num1," / ",Num2," = ",Num1 / Num2)
elif Operation == "4":
    print(Num1," * ",Num2," = ",Num1 * Num2)
else:
    print("Not Valid")
