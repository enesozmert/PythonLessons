

name = "enes"
surname = "ömzert"
age = 99

print("My name is {} {}".format(name, surname))
print("My name is {1} {0}".format(name, surname))
print("My name is {s} {n}".format(n = name, s = surname))
print("My name is {s} {n} and I am {a} years old".format(n = name, s = surname, a = str(age)))

result = 200 / 700
print('the result is {r:1.4}'.format(r=result))

print(f"My name is {name} {surname} and I am {age} years old")