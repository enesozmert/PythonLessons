x, y, z = 5, 10, 20
print(x, y, z)

# x, y = y, x
# print(x,y,z)

x = x + 5;
print(x, y, z)

x += 5
print(x, y, z)

x *= 5
x -= 5
x /= 5
x %= 5
y //= 5
y **= 5
# x |= 5

print(x, y, z)

values = 1, 2, 3, 4, 5
print(type(values))
print(values)

x, y, *z = values
print(values)
print(x, y, z)