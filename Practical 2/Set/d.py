from json.encoder import INFINITY


numbers_set = {23, 234, 54, 45, 65, 87, 64, 546}
mini = INFINITY
max = -INFINITY

for i in numbers_set:
    if(i > max):
        max = i
    
    if(i < mini):
        mini = i


print(f'Numbers set: {numbers_set}')
print(f'Maximum number: {max}')
print(f'Minimum number: {mini}')
