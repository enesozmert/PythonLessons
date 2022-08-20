from cgi import print_form


website = "http://www.google.com"
course = "Python Kursu: Baştan sona Python Programlama Rebhberiniz (40 saat)"

length = len(website)
result = website[7:10]
print(result)
result = website[length - 3:length]
print(result)
result = website[:15]
print(result)
result = website[-15:-1]
print(result)
result = website[-3:]
print(result)
result = course[::-1]
print(result)

s = '12345' * 5
print(s[::5])

name, surname, age, job = 'enes', 'ömzert', 32, 'mühendiske'

result = "Beniim adım " + name + " " + surname + " yaşım " + str(age) + " mesleğim "+ job
print(result)
result = "Benim adım {} {} yaşım {} ve mesleğim {}".format(name, surname, age, job)
print(result)

keyword = "Hello world"
keyword = keyword[0:6] + "W" + keyword[7:]
keyword.replace("w", "W")
print(keyword)

result = 'abc' * 3
print(result)