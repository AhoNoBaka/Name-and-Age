currentYear = input('What is the current year? : ')
name = input('Enter Your Name :')
birthYear = input('Enter your Birth Year :')

while currentYear == '' or name == '' or birthYear == '':
    if currentYear == '':
        print('You haven\'t filled the current year')
        currentYear = input('Please enter the current year: ')
    if name == '':
        print('You haven\'t filled your name: ')
        name = input('Please enter Your Name :')
    if birthYear == '':
        print('You haven\'t filled your Birth year')
        birthYear = input('Please enter your birth year: ')
    

currentYear = int(currentYear)
birthYear = int(birthYear)
age = currentYear - birthYear

print(name)
print(age)
