list_anime = []

while True:
    anime = str(input("Enter the name of an anime (or type 'exit' to finish): "))
    if anime == 'exit':
        print("\nYour anime list includes: ")
        for a in list_anime:
            print(f"- {a}")
        break
    else:
        list_anime.append(anime)
        print(f"{anime} has been added to your list.")
        continue
    
    