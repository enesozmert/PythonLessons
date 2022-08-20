list = [1,2,3]

tuple = (1, 'iki', 3)

print(type(list))
print(type(tuple))

print(len(list))
print(len(tuple))

list = ['ali', 'veli']
tuple = ('damlar', 'ayşe')
names = ('damlar', 'fatma', 'ayşe') + tuple

list[0] = 'ahmet'
# tuple[0] = 'deniz'

countTuple = tuple.count('damlar')
print(countTuple)
print(list)
print(tuple)
print(names)