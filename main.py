print("Welcome to python utilities. our apps:")
print("painted cube solving tool")
print("triangle area finder")
print("slime fighter(game)")
print("time (10 second sample of the date and time)")
command=input("which app do you want to use? ")

if command == "painted cube solving tool":
  import paintedcubesolver
else:
  if command == "triangle area finder":
    import triongle
  else:
    if command == "time":
      import clock
    else:
      import pidms
