car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} # sample car dict

key = input("Enter key: ") # taking key from user

if key in car.keys(): # checking if key exists in dict
    print(f'{key} key is in car dict')
else:
    print(f'{key} key is not in car dict')
