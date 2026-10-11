# Program to find factorial using recursion

# Step 1: Define recursive function
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Step 2: Take input
num = int(input("Enter a number: "))

# Step 3: Call function and print result
print(f"Factorial of {num} is:", factorial(num))
