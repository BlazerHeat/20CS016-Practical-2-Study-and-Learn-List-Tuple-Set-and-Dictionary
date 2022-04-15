print("20CS016 Vatsal Ghoghari")
try:
    a = 10/0
    print (a)
except ArithmeticError:
        print ("Divide by zero.")
else:
    print ("Success.")