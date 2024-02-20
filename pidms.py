smht=120
print("the health of the slime is", smht, "hp do you fight or run?")
attack1=input("attack or run? ")

if attack1=="attack" :
    smht=60
    print("the health of the slime is", smht, "hp do you fight or run?")
    attack2=input("attack or run? ")
    if attack2=="attack" :
        smht=0
        print("the slime ded")
        print("I am python god if work")
    else:
            print("you ran?! Now?")
else:
        print("you ran, bruh")


question=input("do you want to return to home? y/n: ")

if question == "y":
  import main
else:
  print("quitting...")