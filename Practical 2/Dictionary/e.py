dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

dic4 = dic1.copy() # making dic4 copy of dic1
dic4.update(dic2) # merging dic2
dic4.update(dic3) # merging dic3

print(f"dic1: {dic1}")
print(f"dic2: {dic2}")
print(f"dic3: {dic3}")
print(f"dic4: {dic4}")
