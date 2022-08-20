
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
print(val)
val = max(numbers)
print(val)
val = min(letters)
print(val)
val = max(letters)
print(val)

val = numbers[3:6]
print(val)
val = numbers[:3]
print(val)
val = numbers[4:]
print(val)

numbers[4] = 40;
print(numbers)

numbers.append('49')
print(numbers)

numbers.append(49)
print(numbers)

numbers.insert(3, 78)
print(numbers)

numbers.insert(-1, 52)
print(numbers)

numbers.pop()
print(numbers)

# numbers.sort()
# print(numbers)

numbers.reverse()
print(numbers)

print("numbers len: ", len(numbers))
print("numbers len: ", numbers.count(-1))

numbers.clear()
print(numbers)