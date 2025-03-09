import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for n in range(1,1+nr_letters):
    password.append(random.choice(letters))
for n in range(1,1+nr_symbols):
    password.append(random.choice(symbols))
for n in range(1,1+nr_numbers):
    password.append(random.choice(numbers))
print("Your weak password is ", end =" ")
print("".join(password))
strong_pass = []
for n in range(1,1+nr_letters+nr_symbols+nr_numbers):
    tem = random.choice(password)
    strong_pass.append(tem)
    password.remove(tem)
print("Your strong password is ", end =" ")
print("".join(strong_pass))
