string = input("Enter string: ")
output_string = ""
for ch in string:
    if ch.islower():
        output_string += ch.upper()
    else:
        output_string += ch.lower()

print("Swapped: "+output_string)
