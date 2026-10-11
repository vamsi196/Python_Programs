# Program to find the sum of elements in an array using loop (DSA way)

# Step 1: Taking array size as input
n = int(input("Enter number of elements: "))

# Step 2: Taking array elements as input
arr = []
print("Enter the elements:")
for i in range(n):               # loop runs n times
    element = int(input())       # user enters a number
    arr.append(element)          # add number into array

# Step 3: DSA approach: calculating sum using loop
total = 0                        # start with 0
for i in arr:                    # loop through each element
    total += i                   # add element to total

# Step 4: Displaying result
print("The sum of array elements is:", total)
