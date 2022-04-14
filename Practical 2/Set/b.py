from msilib.schema import Error


numbers_set = {1, 2, 4, 5, 6}

print(f"numbers set: {numbers_set}")

num = int(input("Enter number to remove: "))

try:
    numbers_set.remove(num)
except Exception as e:
    pass

print(f"numbers set: {numbers_set}")
