from random import choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")

def take_input():
    while True:
        try:
            count = int(input("How many letters would you like in your password?"))
            return count
        except ValueError:
            print("Please enter an integar number.")

letters_count = take_input()

numbers_count = input("Would you like to add any number? [We highly encourage this] (Yes/No) ").lower()
if numbers_count != 'yes':
    numbers_count = 0
else:
    numbers_count = take_input()

characters_count = input("Would you like to add any number? [We highly encourage this] (Yes/No) ").lower()
if characters_count != 'yes':
    characters_count = 0
else:
    characters_count = take_input()