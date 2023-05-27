import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

p_letters = random.choices(letters,k=nr_letters)
p_symbols = random.choices(symbols,k=nr_symbols)
p_numbers = random.choices(numbers,k=nr_numbers)
r_letters = ''.join(p_letters)
r_symbols = ''.join(p_symbols)
r_numbers = ''.join(p_numbers)

p_list = r_numbers + r_symbols + r_letters
password_pt =[]
for caract in p_list:
    password_pt.append(caract)
random.shuffle(password_pt)

password = ''
for element in password_pt:
    password += element
print(f"Your password is {password}")
