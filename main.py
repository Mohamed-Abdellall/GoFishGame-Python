import random

#Establish players, hands, and deck
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '2', '3', '4', '5', '6', '7', '8', '9',
        '10', '2', '3', '4', '5', '6', '7', '8', '9', '10', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'J', 'K', 'Q', 'A', 'J', 'K', 'Q', 'A', 'J', 'K', 'Q', 'A', 'J', 'K', 'Q', 'A']
myHand = []
botHand = []
myStacks = 0
botStacks = 0
#Dealing of cards to hands
def draw(turn):
    global card
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#Starting out the game
for i in range(5):
    draw(myHand)
    draw(botHand)

#Playing
def askPlayer():
    global botHand

    ask = input("What card would you like?\n")
    if ask in botHand:
        botHand.remove(ask)
        myHand.append(ask)
        print("Bot: Yes.")
    elif ask not in botHand:
        print("Bot: Go fish.")
        card = deck[random.randint(0,len(deck) - 1)]
        deck.remove(card)
        myHand.append(card)

def askBot():
    global myHand

    guess = random.choice(botHand)
    print(f'Bot: Got any...{guess}s?')
    if guess in myHand:
        botHand.append(guess)
        myHand.remove(guess)
        print("Player: Yes.")
    elif guess not in myHand:
        card = deck[random.randint(0, len(deck) - 1)]
        deck.remove(card)
        botHand.append(card)
        print("Player: Go fish.")

#Stacking

def checkStack():

    global botStacks
    global myStacks
    global botHand
    global myHand

    for y in botHand:
        if botHand.count(y) == 4:
            botHand = [i for i in botHand if i != y]
            botStacks += 1

    for y in myHand:
        if myHand.count(y) == 4:
            myHand = [i for i in myHand if i != y]
            myStacks += 1

#The game!
while len(deck) > 1:
    print(myHand)
    askPlayer()
    askBot()
    checkStack()
    if (len(botHand) < 1 or len(myHand) < 1):
        break

print("Your score: " + str(myStacks))
print("Bot's score: " + str(botStacks))

if myStacks > botStacks:
    print("Player Won! Congratulations!")
elif botStacks > myStacks:
    print("Bot Won! Better luck next time!")
elif botStacks == myStacks:
    print("Draw! Close game!")