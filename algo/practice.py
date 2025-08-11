from collections import defaultdict

# Don't shadow built-in map()
group_map = defaultdict(list)

a = {'name': 'x', 'dob': 1982}
b = {'name': 'y', 'dob': 1990}
c = {'name': 'z', 'dob': 2000}
a1 = {'name': 'x3', 'dob': 2001}

start = 1
arr = []
arr.append(a)
arr.append(b)
arr.insert(1, c)
arr.append(a1)

print(arr)

for i in range(len(arr)):
    if group_map:  # same as len(group_map) > 0
        placed = False
        for index, items in list(group_map.items()):  # list() to avoid issues if dict grows
            if items and arr[i]['name'][0] in items[0]['name']:
                group_map[index].append(arr[i])
                placed = True
                break
        if not placed:
            group_map[start + i].append(arr[i])
    else:
        group_map[start + i].append(arr[i])

for item in group_map.items():
    print(item)
