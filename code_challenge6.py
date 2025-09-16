total = 0

for i in range(7): 
    num = eval(input("Enter a number: "))
    if num % 2 != 0: 
        total += num

print("The sum of all odd numbers is", total)