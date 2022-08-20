name = "enes"
surName = "ömzert"
age = 90

greeting = "My name is " + name + ' ' + surName + ' ' + "\nI am " + str(age) + " years old."
length = len(greeting)

print(greeting)
print(greeting[0])
print(greeting[1])
print("end char : " , greeting[length - 1])
print("end char : " , greeting[-1])
print("char[or] : " , greeting[3:7])
print("char[or-end] : " , greeting[3:])
print("char[start-or] : " , greeting[:15])
print("char[start-or-step] : " , greeting[2:15:2])
print(length - 1)