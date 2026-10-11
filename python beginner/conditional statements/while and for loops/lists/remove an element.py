#s = {1, 2, 3, 4, 5}

#s.discard(3)   # safely removes element
#print("After removing:", s)




'''set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)'''


t = (1, 2, 3, 2, 4, 5)

if len(t) == len(set(t)):
    print("No duplicates")
else:
    print("Contains duplicates")

