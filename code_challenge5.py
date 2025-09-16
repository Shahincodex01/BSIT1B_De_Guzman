number = eval(input("Enter any number --> "))
x = 1

for i in range(number, 0, -1):
    x *= i
    print("The Factorial of", number, "is", x)

print("The final answer is:", x)