numbers = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

sum = 0

for i in numbers.values():
    sum += i

print(f"numbers dict: {numbers}")
print(f"sum of items: {sum}")