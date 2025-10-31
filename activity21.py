soDirty = True 
sum = 0
while soDirty == True:
    wash = input("Do you wish to continue the washing? (yes / no )").lower()
    sum += 1
    if wash == 'yes':
        print("Washing Continues...")
        continue
    else:
        print("Washing Stops...")
        break
print(f"You've washed {sum} times")