"""
Müşteri adı
soyadı 
ad + soyad
cinsiyet
tc kimlik
doğum yılı
adres bilgisi
yaşı
"""
nowDate = 2021
customerName = "Enes"
customerSurname = "Ömzert"
customerFullName = customerName + customerSurname
customerGender = True
customerId = '1123213213213'
customerBirth = 1999
customerAdress = "İstanbul"
customerAge = nowDate - customerBirth

"""
sipariş 1 => 110
2 => 1100.5
3 => 356.95
"""

order1 = 110
order2 = 1100.5
order3 = 356.95

result = order1 + order2 + order3
print("result order :" , result)