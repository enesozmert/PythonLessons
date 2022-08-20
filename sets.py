
fruits = {'orange', 'apple', 'banana'}

print(fruits)
for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango', 'grape', 'apple'])
print(fruits)

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList))

fruits.remove('mango')
fruits.discard('mango')
fruits.pop()
print(fruits)