#**********************DATA SCIENCE ***********************

#Question 1
Even=[]
for i in range (1,11):
    E=int(input("Enter the list of 10 numbers: "))
    if E%2==0:
        Even.append(E)
print("The Even values from the list is",Even)

#Question 3
Number=int(input("Enter the number: "))
d={}
for i in range(1,Number+1):
    d[i]=i*i

print("The output dic is:\n",d)

#Question 4:
import math
x, y = 0, 0
Number=int(input("Enter the number of steps need to perform: "))
i=1
for  i in range(Number):
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = round(math.sqrt(x**2 + y**2))

print("Distance:", c)

