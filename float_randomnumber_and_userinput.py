#Playing around with two floating point numbers, first is being generated randomly and second is deriving from user input. Print formatting with different decimals.

import random

#Generating a floating point number which will be our first number
first_number = random.uniform(0, 100)

#Prompting user for input -> getting our second number
second_number = float(input("Please enter a floating point number:"))

#Making the first, randomly generated number visible (with two decimals only)
print(f"The first, generated floating point number is {first_number:.2f}")

#Sum calculation assignment
sum_numbers = first_number + second_number


#printing sum based on conditions, using comparison operators and statements
if sum_numbers < 10.1:
	print(f"The sum of your numbers is {sum_numbers:.2f}, which is less than 10.1")
elif 10.1 <= sum_numbers <= 20.1:
	print(f"The sum of your numbers is {sum_numbers:.2f}, which is between the range of 10.1 and 20.1")
else:
	print(f"The sum of your numbers is {sum_numbers:.2f}, which is bigger than 20.1 ")

#Substraction assignment
subst_numbers = first_number - second_number

#printing the result using comparison operators and statements
if subst_numbers >= 0.1:
	print(f"The result of the substraction is positive, result is {subst_numbers:.2f}")
elif 0.1 >= subst_numbers >= 0:
	print(f"The result of the substracion is {subst_numbers:.1f} falls in the range of numbers between 0 and 0.1 ")
else:
	print(f"The result of the substraction is {subst_numbers:.2f}, number is negative ")

#Printing the square of sum_numbers with 3 decimals
square_of_sum = sum_numbers ** 2
print(f"The square of your sum is {square_of_sum:.3f}")

#Printing the square root of sum_numbers with 3 decimals
square_root_sum = sum_numbers ** 0.5
print(f"The square root of your sum is {square_root_sum:.3f}")