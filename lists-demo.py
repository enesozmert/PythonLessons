cars = ["Bmw", "Mercedes", "Opel", "Mazda"]
cars_count = len(cars)
print(cars_count)
cars[-1] = "Toyata"
result = cars
print(result)
result = "Mercedes" in cars
print(result)
result = cars[0:3]
print(result)
cars[-2:] = ["Toyata", "Renault"]
result = cars
print(result)
result = cars + ["Audi", "Nissan"]
cars = result
print(result)
del cars[-1]
print(cars)
result = cars[::-1]
print(result)

studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentA = ["Sena", "Turan", 1999, [80,60,70]]
studentA = ["Ahmet", "Turan", 1990, [80,60,40]]