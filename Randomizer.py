import random
import string
from colorama import init, Fore
from colorama import Back
from colorama import Style
y = 1
init(autoreset=True)
def random_string(length=32):
	character_set = string.ascii_letters
	return ''.join(random.choice(character_set) for i in range(length))

print("$ Author Cisamu")
print("$ All rights reserved (c)2022")
print("Available colors: Green, Blue, Red, White")
randomuser = input("ENTER COLOR TO GENERATE:")
if randomuser == "Green":

	my_random = random_string(999999)

	while y<5:
		print(Fore.GREEN + my_random)

elif randomuser == "White":
	my_random = random_string(999999)

	while y<5:
		print(my_random)

elif randomuser == "Blue":
	my_random = random_string(999999)

	while y<5:
		print(Fore.BLUE + my_random)
elif randomuser == "Red":
        my_random = random_string(999999)

while y<5:
		print(Fore.RED + my_random)

while y<5:
		print(my_random)
else:
    print("Color not found")
#Author Cisamu
#All rights reserved (c)2022