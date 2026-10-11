def linear_search(arr,target):
    for i in range(len(arr5)):
        if arr[i]==target:
            return i
    return-1
n=int(input("enter number of elements:"))
arr=[]
print("enter the elements:")
for i in range(n):
    arr.append(int(input()))

target=int(input("enter the element to search:"))
result=linear_search(arr,target)
if result !=-1:
    print(f"element found at index {result}")
else:
    print("element not found")