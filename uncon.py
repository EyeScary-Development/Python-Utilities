print("convert to miles (1) or kilometers (2)? \n")
un=input(: )
if un == 1:
    num1=input("input number in kilometers")
    print("\n \n" num1,"km in miles is", num1*1.6,"miles. Cause we hate kilometers")
    if question == "y":
     import main
    else:
     print("quitting...")
else:
    num1=input("input number in miles")
    print("\n \n" num1,"km in miles is", num1/1.6,"kilometers. Cause we are the EU")
    question=input("do you want to return to home? y/n: ")
    if question == "y":
     import main
    else:
     print("quitting...")