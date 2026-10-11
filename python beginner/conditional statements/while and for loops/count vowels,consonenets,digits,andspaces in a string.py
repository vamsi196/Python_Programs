s=input("enter a string:")
vowels=0
consonents=0
digits=0
spaces=0
for ch in s:
    if ch.lower() in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consonents+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces+=1
print("vowels:",vowels)
print("consonents:",consonents)
print("digits;",digits)
print("spaces:",spaces)
