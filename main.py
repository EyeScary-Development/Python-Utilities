print("Welcome to python utilities. our apps:")
print("painted cube solving tool")
print("calculator")
print("triangle area finder")
print("slime fighter(game)")
print("time (10 second sample of the date and time)")
print("2d area calculator")
print("3d volume calculator")
print("dictionary")
print("random number generator")
print("unit converter (miles to kilometers, kilometers to miles)")
command=input("which app do you want to use? ")

if command == "painted cube solving tool":
  import paintedcubesolver
elif command == "triangle area finder":
  import triongle
elif command == "time": 
    import clock
elif command == "2d area calculator":
  import arcalc
elif command == "3d volume calculator":
  import volcalc
elif command == "dictionary":
  import diction
elif command == "Calculator" or command == "calculator":
  import calculator
elif command == "random number generator":
  import radnom
elif command == "unit converter":
  import uncon
else:
      import pidms
