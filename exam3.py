import func
import random

choices = ['bird','dog','snake','fish','cat','mouse','starfish','woodchuck','crab']
#randomizes choices
def board(choices):
    
    rand = random.randrange(0, 9)
    #appends the randomly assigned choices
    choices.append(choices[rand])
    #shuffles the choices in the array so that the game board is always different
    random.shuffle(choices)
    
    return choices

#checks the cards picked and ensures tha0t the user enters valid inputs
def cardPicked(first, second):
    
    if first > 9 or first < 0 or second > 9 or second < 0 or first == second:
        print "Invalid Input! You must pick different cards and the card must be a number from 0-9.\n"
        return False
    else:
        return True
        
def main():
    #create the game board with the cards
    board(choices)
    tries = 0 
       
    play = True
    while play:
        tries += 1 #add 1 each time user plays to keep track of how many tries it took them to win
        first = func.userInt("Pick the first card to turn over (0-9): ")
        second = func.userInt("Pick the second card to turn over (0-9): ")
        #prints out the cards user picked
        print "Card {} is a {}.".format(first, choices[first])
        print "Card {} is a {}." .format(second, choices[second])
    
        cardPicked(first,second)
        if first == second:
            "Can't pick same card"
        #if user's first and second choice were the same cards then they will be prompted that they won
        elif choices[first] == choices[second]:
            print "You win! It took you {} tries." .format(tries)
        
main()