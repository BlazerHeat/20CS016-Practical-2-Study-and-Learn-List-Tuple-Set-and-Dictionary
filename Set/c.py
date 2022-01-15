set1 = {1, 2, 3,  4}
set2 = {3, 4, 5, 6}

set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set1 union set2: {set3}")
print(f"set1 intersection set2: {set4}")
print(f"set1 difference set2: {set5}")
