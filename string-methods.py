

message = "Hello There. My name is Enes Ozmert"

message = message.upper()
print(message)
message = message.lower()
print(message)
message = message.title()
print(message)
message = message.capitalize()
print(message)

message1 = " Hello There. My name is Enes Ozmert"
message1 = message1.strip()
print(message1)
message1 = message1.split('.')
print(message1[1].strip())
message1 = ' message1'.join(message1)
print(message1)

message2 = "Abcdefg"
index = message2.find('bc')
print(index)

isFound = message2.startswith('H')
print(isFound)

isFound = message2.endswith('g')
print(isFound)

message2 = message2.replace("A", "Z")
print(message2)

message2 = message2.center(100, "*")
print(message2)