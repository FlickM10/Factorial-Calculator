X = int(input("Enter a value for X to calculate its factorial value : "))
if X <= 0:
    print("-9999")
else:
    fact = 1
    while X > 0:
        fact = fact * X
        X = X - 1  
    print("The factorial is :", fact)