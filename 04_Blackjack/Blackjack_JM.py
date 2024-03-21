""" OPIS """

import random, sys

# Playing card suits
HEARTS   = chr(9829) # Znak 9829 to '♥'.
DIAMONDS = chr(9830) # Znak 9830 to '♦'.
SPADES   = chr(9824) # Znak 9824 to '♠'.
CLUBS    = chr(9827) # Znak 9827 to '♣'.

# Backside of card (hidden card)
BACKSIDE = "hidden"

""" Main program loop """
def main():
    budget = 5000
    while True:

        # Check the budget
        if budget <= 0:
            break

        # The Bet
        print("Current budget: {} euro" .format(budget))
        bet = getBet(budget)

        # Prepare cards
        deck = getDeck()
        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]
        displayHands(playerHand,dealerHand,False)
        

        #Player's move
        while True:

            if getHandValue(playerHand) > 21:
                break
            #################################
            #value = getHandValue(playerHand)
            #print("Value: {}".format(value))
            #################################
            move = getMove()
            if move == 'M':
                if bet*2 <= budget:
                    bet *= 2
                else:
                    print("You don't enough to make double bet")
                    continue

            if move in ('D','M'):
                playerHand.append(deck.pop())

                if getHandValue(playerHand) > 21:
                #displayHands(playerHand,dealerHand,False)
                    continue

            if move in ('M','P'):
                break


        # Dealer's move
        if getHandValue(playerHand) <= 21:
            while True: 
                if getHandValue(dealerHand) >= 17:
                    break

                print("Dealer draws a card...")
                dealerHand.append(deck.pop())
            
        # Display Hand
        print("Let's check the winner...")
        displayHands(playerHand,dealerHand,True)

        # Check winner
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if playerValue > 21:
            print("You got above 21! You lost this round.")
            budget -= bet
        elif dealerValue > 21:
            print("Dealer got above 21! He lost this round!")
            budget += bet
        elif playerValue > dealerValue:
            print("You got above the dealer! You won this round!")
            budget += bet
        elif playerValue == dealerValue:
            print("Looks like we've got a tie...")

    print("Oh well... looks like You are broke.")


def getBet(maxBudget):
    """ Asking player for bet"""

    print("How much do You want to bet? or You want to (E)nd the game?")
    while True:
        bet = input('> ')

        if bet.upper().strip() == 'E':
            print("Thank You for game,")
            print("You have finished game with...")
            if maxBudget > 5000:
                print("Wow, You got {} dollars!".format(maxBudget))
            else:
                print("Well... {} dollars.".format(maxBudget))
            sys.exit()
        
        if not bet.isdecimal():
            print("Please for a proper bet...")
            continue

        bet = int(bet)
        if 1 < bet <= maxBudget:
            return bet
        
        print("Your bet must be between 1 and {}".format(maxBudget))


def getDeck():
    """ Preparing deck """
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        # NUMBER CARDS
        for rank in range(2, 11): # SPRAWDZIĆ DLA 10 DLA ZASADY
            deck.append((str(rank), suit))
        # FIGURE CARDS
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((str(rank), suit))

    random.shuffle(deck)
    return deck

def displayHands(playerHand,dealerHand,showDealerHand):
    
    if showDealerHand:
        displayCards(dealerHand)
    else:
        displayCards([BACKSIDE] + dealerHand[1:])

    displayCards(playerHand)




def displayCards(cards):
    """ Show cards depending on their rank and suit """
    rows = ['','','','','']

    for i, card in enumerate(cards):
        if card == BACKSIDE:
            rows[0] += ' ___   '
            rows[1] += '|#  |  '
            rows[2] += '| # |  '
            rows[3] += '|__#|  '
            rows[4] += '       '
        else:
            rank, suit = card
            rows[0] += ' ___   '
            rows[1] += '|{} |  '.format(rank.ljust(2,' '))
            rows[2] += '| {} |  '.format(suit)
            rows[3] += '|_{}|  '.format(rank.rjust(2,'_'))
            rows[4] += '       '

    for row in rows:
        print(row)

def getMove():
    '''Get the players move'''
    possibleMoves = ['D','M','P']
    print("What is your move?")
    while True:
        print("(D)raw a card / (M)ake a double bet / (P)ass")
        move = input('> ')

        move = move.upper().strip()
        if move in possibleMoves:
            return move
        else:
            print("Incorrect move")

def getHandValue(hand):
    value = 0
    for card in hand:
        rank = card[0]
        if rank == 'A':
            value += 1
            if value <= 11:
                value += 10
        elif rank in ('J','Q','K'):
            value += 10
        else:
            value += int(rank)

    return value









if __name__ == '__main__':
    main()