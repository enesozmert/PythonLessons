
sehirler = ['kocaeli', 'istanbul']
plakalar = [41, 34]

result = plakalar[sehirler.index('kocaeli')]
print(result)

#plakalar = {'key': 'value'}
plakalar = {'kocaeli': 41, 'istanbul': 34}
print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['ankara'] = 6;
plakalar['kocaeli'] = '41 kere maşallah'

print(plakalar)

users = {
    'enesozmert' : {
        'age' : 36,
        'roles':['admin', 'user'],
        'email': 'ontebeach@gmail.com',
        'adress': 'islamabat',
        'phone': '249394*2',
    },
    'ebulhasimi' : {
        'age' : 16,
        'roles':['user'],
        'email': 'ontebeach@gmail.com',
        'adress': 'islamabat',
        'phone': '249394*2',
    }
}

print(users['enesozmert']['age'])
print(users['enesozmert']['roles'][0])