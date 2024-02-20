x= float(input("input the width of the triangle "))
y= float(input("input the height of the triangle "))
result= (x*y)/2
print("the area of your triangle is", result, "units squared")

question=input("do you want to return to home? y/n: ")

if question == "y":
  import main
else:
  print("quitting...")