website = "http://www.google.com"
course = "Python Kursu: Baştan sona Python Programlama Rebhberiniz (40 saat)"

result = " Hello World ".strip()
print(result)
result = " Hello World ".lstrip()
print(result)
result = " Hello World ".rstrip()
print(result)

result = website.lstrip('/:pth')
print(result)

result = website.strip('w.moc')
print(result)

result = website.count('a')
print(result)
result = website.count('www', 0 ,10)
print(result)

result = website.startswith('www')
print(result)
result = website.endswith(".com")
print(result)

result = website.find("com")
print(result)
result = website.find("com", 0, 10)
print(result)
result = course.rfind("Python")
print(result)

result = website.index("com")
print(result)
result = website.rindex("com")
print(result)

result = course.isalpha()
print(result)
result = course.isdigit()
print(result)

result = 'Contents'.center(50,'i')
print(result)
result = 'Contents'.ljust(50,'i')
print(result)
result = 'Contents'.rjust(50,'i')
print(result)
result = course.replace(' ', '-')
print(result)
result = course.replace(' ', '-', 3)
print(result)

result = course.split(' ')
print(result)