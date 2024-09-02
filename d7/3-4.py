#4 sum of digits in list
#-----------------------
# Prompt user for input
L= input("Enter a list of integers separated by spaces: ")

# Convert input string into a list of integers
x = list(map(int,L.split()))

sums = []  # List to hold the sum of digits of each number

i = 0
while i < len(x):
    num = x[i]
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    sums.append(digit_sum)  # Add the sum of digits to the list
    i += 1

print(f"the sum of your list digits:{sums}")

 
