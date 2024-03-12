import random
print("welcome to generate number")
num1=float(input("input lowest boundary"))
num2=float(input("input highest boundary"))
print(random.randint(num1,num2))
question=input("do you want to return to home? y/n: ")

if question == "y":
  import main
else:
  print("quitting...")