#Playing around with a list (containing integers), practicing comparison operators and statements e.g. freshly learnt 'for loop'.
import random
#First step: Generate a random list of integers between 1 and 15 - 10 numbers in total
random_list_integers = [random.randint(1, 15) for _ in range(10)]
#Printing our random list of integers
print(f"The randomly generated list of integers is: {random_list_integers}")
#Printing a sorted version of this list without modifying the original list
sorted_list = random_list_integers.copy()
sorted_list.sort()
print(f"Sorted version of our randomly generated is: {sorted_list}")
#Even or odd with for loop
for num in random_list_integers:
	if num % 2 == 0:
		print(f"Even number -> {num}")
	else:
		print(f"Odd number-> {num}")

#Picking index position '1' - so picking the second number of our list and playing with comparison operators and statements
if random_list_integers[1] >10:
	print(f"The second number in your list is bigger than 10 ")
elif random_list_integers[1] == 10:
	print(f"The second number in your list equals to 10")
else:
	print(f"The second number in your list is less than 10")

#Checking the sum of integers within our randomly generated list using for loop
list_sum = 0

for num in random_list_integers:
	list_sum = list_sum+num

print(f"The sum of integers in your randomly generated list is {list_sum}")

#Printing the square, and square root of the first number in the random list
square_in_list = random_list_integers[0] ** 2
square_root_in_list = random_list_integers[0] ** 0.5

print(f"The square of your first number in the random list is {square_in_list}  \nThe square root of your first number in the random list is {square_root_in_list}")