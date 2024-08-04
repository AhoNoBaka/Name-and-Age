def validation(prompt, validation_func):
    user_input = input(prompt)
    while not validation_func(user_input):
        print("Invalid input:", user_input)
        user_input = input(prompt)
    return user_input

def number(input_string):
    return input_string.isdigit()

def letter(input_string):
    return input_string.isalpha()

currentYear = validation('What is the current year? : ', number)
name = validation('Enter Your Name :', letter)
birthYear = validation('Enter your Birth Year :', number)

currentYear = int(currentYear)
birthYear = int(birthYear)
age = currentYear - birthYear

print(name, "is currently", age, "years old at the year", currentYear)
