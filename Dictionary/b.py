dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print("Before merge:")
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")

dict1.update(dict2) # merging dict2 in dict1

print("After merge:")
print(f"dict1: {dict1}")
