import random
slmht=12
slmatk=1
slmdef=1
plhth=25
platk=2
pldef=2
ha=3


while slmht > 0:
  print("The slime has", slmht, "health, you have", plhth, "Do you attack, run or heal")

  choice=input("attack, run or heal?: ")
  slmatkon=random.randint(0,1)
  helhelt= plhth+ha
  attack=random.randint(1,2)


  if choice == "attack":
    slmht=slmht-attack
    print("you attacked the slime. It's health is now:", slmht)

  elif choice == "heal":
    if helhelt >= 25:
      print("You cannot heal at this high health")
    else:
      plhth += ha
      print("You healed", ha, "health. You now have", plhth, "health")
  elif choice == "run":
    print("You ran away, seriously?")
    command=input("return home? y/n: ")
    if command == "y":
      import main
    else:
      print("quitting...")


  if slmatkon == 1:
    plhth -= slmatk
    print("The slime attacked you! you have", plhth, "health")

  if plhth < 1:
    print("the you is die")
    command=input("return home? y/n: ")
    if command == "y":
      import main
    else:
      print("quitting...")

  if slmht < 1:
    print("The slime is die")
    command=input("return home? y/n: ")
    if command == "y":
      import main
    else:
      print("quitting...")
