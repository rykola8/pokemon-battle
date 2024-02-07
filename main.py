
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons")
    print("3. Top 10 weakest pokemons")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        number = input('choose pokemon number: ')
        x = pokemons[int(number)]
        print(x)
        pass
    elif choice == '2':
        def myfunc(attacks):
            return attacks['attack']
        pokemons.sort(key = myfunc, reverse = True)
        print(pokemons[0:9])
        pass
    elif choice == '3':
        def myfunc(attacks):
            return attacks['attack']
        pokemons.sort(key = myfunc)
        print(pokemons[0:9])
        pass
    elif choice == '4':
        import random
        pokemon1 = random.choice(pokemons)
        print(pokemon1)

        number = input('choose pokemon number: ')
        pokemon2 = pokemons[int(number)]
        print(pokemon2)

        health1 = pokemon1["total"]
        health2 = pokemon2["total"]

#
        while True:
            import random
            random_number = random.randint(1, 9)
            print("Your random number is", random_number)

            damage1 = int(pokemon2['attack']) -  int(pokemon1['defense']) + random_number
            damage2 = int(pokemon1['attack']) -  int(pokemon2['defense']) + random_number
            if damage1 < 0:
                damage1 = 0
            if damage2 < 0:
                damage2 = 0    
            health1 = health1 - damage1
            health2 = health2 - damage2

            if health1 < 0:
                print("Pokemon 2 is winner;", "Pokemon 2 health is: ", health2)
                break
            elif health2 < 0:
                print("Pokemon 1 is winner;", "Pokemon 1 health is: ", health1)
                break
            
 #       pass

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


