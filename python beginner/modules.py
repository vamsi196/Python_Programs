arr=[1, 2, 3, 2]
map = {}
for num in arr:
    if num not in map:
        map[num]=1
    else:
        map[num] = map[num] +1
for (key, val) in map.items():
    if val>1:
        print(key)
        break
