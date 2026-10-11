s = input("Enter a string: ")

for ch in s:
    if s.count(ch) == 1:   # appears only once
        print("First non-repeating character:", ch)
        break
