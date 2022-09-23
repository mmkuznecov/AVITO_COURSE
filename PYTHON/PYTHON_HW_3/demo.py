from advert import JsonParser, Advert
import json

with open ('example1.json', 'r') as f:

    data = json.load(f)

adv = Advert(data) # initialization from dict

# let's check attributes

print('--------------------------------')

print(adv.__dict__)
print(adv.title)
print(adv.price)
print(adv.location.address)

# let's check class sample output

print('--------------------------------')

print(adv)

adv.repr_code_color = 32

print(adv)

adv.repr_code_color = 33

print(adv)

print('--------------------------------')

# let's check we can't set price with negative value

try:
    adv.price = -100
except Exception as e:
    print(e)

# and finally let's check we check situation with keywords

with open ('example2.json', 'r') as f:

    data = json.load(f)

adv2 = Advert(data)

print('--------------------------------')

print(adv2.__dict__)
print(adv2.class_)

print('--------------------------------')

# and two more examples - with negative price and without title

print('--------------------------------')

with open ('example3.json', 'r') as f:
    data = json.load(f)

try:
    adv3 = Advert(data)
except Exception as e:
    print(e)

print('--------------------------------')

print('--------------------------------')

with open ('example4.json', 'r') as f:
    data = json.load(f)

try:
    adv4 = Advert(data)
except Exception as e:
    print(e)

print('--------------------------------')