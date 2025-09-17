print("PARROT SIMULATOR - THE ECHO CHAMBER!")
parRot = input("What do you want your parrot to say?: ")
howmAny = eval(input("How many times should the parrot squawk it?: "))
sQuawk = "🦜 Squawk!"

for i in range(howmAny, 0, -1):
    print(sQuawk, parRot)