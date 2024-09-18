list = []

for i in range(5):
    Num = int(input("Enter a whole number"))
    list.insert(i-1, Num)



def BubbleSort():
    for i in range(len(list)):
        if list[0] > list[1]:
            Change = list[0]
            Change1 = list[1]
            list[0] = Change1
            list[1] = Change
        if list[1] > list[2]:
            Change = list[1]
            Change1 = list[2]
            list[1] = Change1
            list[2] = Change
        if list[2] > list[3]:
            
            Change = list[2]
            Change1 = list[3]
            list[2] = Change1
            list[3] = Change
        if list[3] > list[4]:
            Change = list[3]
            Change1 = list[4]
            list[3] = Change1
            list[4] = Change
        print(list)
        
BubbleSort()
