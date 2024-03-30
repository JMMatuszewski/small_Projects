import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}
purse = 100

#Bets:
#   - CHO - parzyste
#   - HAN - nieparzyste

while True:
    if purse <= 0:
        print("Looks like You are broke")
        sys.exit()

    #Make a bet
    print("How much do You put on the table?")
    print("or do You want to (E)nd the game?")
    print()
    #Check if bet is correct
    while True:
        bet = input("> ")
        if bet.upper() == "E":
            print("You finished with {} in your purse.".format(purse))
            sys.exit()
        elif bet.isdecimal():
            bet = int(bet)
            if bet > purse:
                print("You don't have this much money...")
                continue
            break
        else:
            print("Please make a correct bet.")

    #Roll the dices
    print("Dealer is throwing dices.")
    input("press enter to continue...")
    print()
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)

    #Make a guess.
    print("What is your guess?")
    print("- CHO - even")
    print("- HAN - odd")
    print()
    while True:
        guess = input("> ")
        if guess.upper() != "CHO" and guess.upper() != "HAN":
            print("You made not acceptable guess - only CHO or HAN")
            continue
        break
        
    if (dice1 + dice2) % 2 == 0:
        result = "CHO"
    else:
        result = "HAN"

    #Check the bet
    print("We got...")
    print("{} and {},".format(JAPANESE_NUMBERS[dice1],JAPANESE_NUMBERS[dice2]))
    print("which is {} and {}.".format(dice1,dice2))
    print()
    if result == guess:
        print("You won the bet!")
        purse += bet
    else:
        print("You lost the bet.")
        purse -= bet
    
    print("You have {} in your purse.".format(purse))
    input("Press enter to continue...")
    print()
