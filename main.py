name = input('Enter Your Name :')
age = input('Enter your Birth Year :')

while name == '' or age == '':
    if name == '':
        print('Wala ka pangalan')
        name = input('Enter Your Name :')
    if age == '':
        print('Wala kang nilagay na birth year')
        age = input('Enter your birth year')

age = int(age)
age = 2024 - age

print(name)
print(age)
