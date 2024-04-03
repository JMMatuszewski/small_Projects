
import sys,random

"""Main loop"""
while True:

    # Get the request
    print("Do You want to (E)nd, or give the dices to be thrown?")
    strDice = input("> ")

    # Check of exit
    if strDice.upper() == "E":
        sys.exit()
    
    # Ditch the empty spaces
    strDice = strDice.lower().replace(' ','')

    # Get the index of sepator
    indexD = strDice.find('d')

    # Digest the string for proper parts
    if indexD == -1:
        print("Please don't forget about the D!")
        continue

    # Get the number of dices
    diceNumber = strDice[:indexD]

    if not diceNumber.isdecimal():
        print("Please give the correct number of dices")
        continue
    elif not diceNumber:
        print("Guess You meant there is only 1 dice...")
        dices = 1
    else:
        dices = int(diceNumber)

    # Check for mod
    indexMod = strDice.find('+')
    if indexMod == -1:
        indexMod = strDice.find('-')

    # Get the nubmer of sides
    if indexMod == -1:
        numberOfSides = strDice[indexD+1:]
    else:
        numberOfSides = strDice[indexD+1:indexMod]
    
    # Check for correct side number
    if not numberOfSides.isdecimal():
        print("Please give correct number of sides")
        continue
    numberOfSides = int(numberOfSides)

    # Check and get the number for mode
    if indexMod == -1:
        numberMod = 0
    elif strDice[indexMod+1 : ] and strDice[indexMod+1 : ].isdecimal():
        if strDice[indexMod] == '-':
            numberMod = -int(strDice[indexMod + 1 :])
        else: 
            numberMod = int(strDice[indexMod + 1 :])
    else:
        print("Please give correct number for mode")
        continue

    # Roll the dices
    doneDices = []
    for i in range(dices):
        roll = random.randint(1,numberOfSides)
        doneDices.append(roll)

    # Callculate the rolls
    result = 0
    for d in doneDices:
        result += d
    result += numberMod

    # Show the rolls and result
    print("The rolls:")
    print(doneDices)
    if not indexMod == -1:
        print("...with mode {}".format(numberMod))
    print("Result: {}".format(result))

    
        

