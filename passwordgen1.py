import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
'w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y'
,'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')']
print("Hello There ! Welcome to my Password Generator :)")
nr_letters = int(input("So , How many Letters you want to insert in your Password"))
nr_numbers = int(input("So , How many Numbers you want to insert in your Password"))
nr_symbols = int(input("So , How many Symbols you want to insert in your Password"))

password = ""

for char in range (1,nr_letters+1):
    password+=random.choice(letters)

for char in range (1,nr_numbers+1):
    password+=random.choice(numbers)

for char in range (1,nr_symbols+1):
    password+=random.choice(symbols)

print(password)


