import func
rank = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suit = ['Clubs','Hearts','Diamonds','Spades']

def buildDeck(rank, suit):

    deck = ['{} of {}'.format(r, s) for r in rank for s in suit]
    return deck
    
def shuffle(deck):
    deck2 = (deck[:26])
    deck3 = (deck[26:])
    shuffledDeck = []
    i = 0
    
    while i < len(deck2) and i < len(deck3):
        shuffledDeck.append(deck2[i])
        shuffledDeck.append(deck3[i])
        i += 1

    for x in range(i, len(deck2)):
        shuffledDeck.append(deck3[x])
    
    for x in range(i, len(deck3)):
        shuffledDeck.append(deck3[x])
    return shuffledDeck


def deal(deck):
    topDeck = deck[:5]
    return topDeck

def main():
    deck = buildDeck(rank,suit)
    userInput = func.userInt("How many times do you want me to shuffle?")
    x = 0
    while x < userInput:
        deck = shuffle(deck)
        x += 1
    print deal(deck)
    
main()
    