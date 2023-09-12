import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")

def take_input(x):
    while True:
        try:
            count = int(input(f"How many {x} would you like in your password? "))
            return count
        except ValueError:
            print("Please enter an integar number.")

letters_count = take_input('lettters')

numbers_count = input("Would you like to add any number? [We highly encourage this] (Yes/No) ").lower()
if numbers_count != 'yes':
    numbers_count = 0
else:
    numbers_count = take_input('numbers')

characters_count = input("Would you like to add any special characters? [We highly encourage this] (Yes/No) ").lower()
if characters_count != 'yes':
    characters_count = 0
else:
    characters_count = take_input('special characters')


# password generate

password = ''

def generate_password(element_list, element_count):
    password = ''
    for _ in range(element_count):
        password += random.choice(element_list)
      
    return password

password += generate_password(letters, letters_count)
password += generate_password(numbers, numbers_count)
password += generate_password(special_characters, characters_count)

password = list(password)

random.shuffle(password)

password = ''.join(password)

print(f'Your password is: {password}')