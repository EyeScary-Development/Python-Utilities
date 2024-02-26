w=float(input("input the width of your box "))
h=float(input("input the height of your box "))
d=float(input("input the depth of your box "))

print("your box has a volume of", w*h*d, "units squared")

command=input("return to home? y/n ")
if command == "y":
    import main
else:
    print("quitting...")