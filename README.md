# Factorial-Calculator
A simple python program to calculate the factorial value of any number!

# 🛠️ Code Components and Logic
1.Input and Initialization

    X = int(input("Enter a value for X to calculate its factorial value : "))
The script first prompts the user to enter an integer value and stores it in the variable X.

2. Validation and Error Handling

       if X <= 0:
        print("-9999")
This if statement checks if the input value X is less than or equal to zero ($X \le 0$).If the condition is True (meaning the input is zero or a negative number), it prints the string "-9999", which serves as a simple error code indicating an invalid input for this specific calculation.

3. Factorial Calculation (for $X > 0$)

        else:
        fact = 1
        while X > 0:
           fact = fact * X
           X = X - 1  
        print("The factorial is :", fact)
If $X$ is a positive integer (the else block executes):
fact = 1: A variable fact is initialized to $1$.This is the starting point for the product.

while X > 0: The code enters a loop that continues as long as the value of X is greater than $0$.

fact = fact * X: In each iteration, the current value of $X$ is multiplied by the running product stored in fact.

X = X - 1: $X$ is then decremented by $1$.This loop effectively calculates the factorial $X! = X \times (X-1) \times (X-2) \times \dots \times 1$.

Once the loop finishes (i.e., when $X$ becomes $0$), the final result stored in fact is printed.
