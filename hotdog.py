import random
import time
import func

def calculate(predictedWinner):
    tom = 0
    sally = 0
    fred = 0
    
    tomWin = False
    sallyWin = False
    fredWin = False
    
        
    while True:
        #randomly increment tom's, sally's and fred's total numbers
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        c = random.randint(1, 9)
        tom += a
        sally += b
        fred += c
          
        #if the contestant goes over 50, it will assign the total number to 50 and break out of the loop 
        if tom >= 50:
            tom = 50
            tomWin = True
            break
        
        if sally >= 50:
            sally = 50
            sallyWin = True
            break
                
        if fred >= 50:
            fred = 50
            fredWin = True
            break
            
        print "Chomp...  Chomp...  Chomp \n"
        print "Tom has eaten %s hot dogs!" %tom
        print "Sally has eaten %s hot dogs!" %sally
        print "Fred has eaten %s hot dogs!\n" %fred
       
        time.sleep(1)
    
    #returns the total numbers for each contestant in a tuple
    return (tomWin, sallyWin, fredWin)
        

def askUser():
    #ask user input and turn it to lowercase
    winner = func.userString("Who do you think will win? (Tom, Sally or Fred)")
    winner = winner.lower()
    return winner
    
def main():
    predictedWinner = askUser()
    winners = calculate(predictedWinner)
    
    #print out the winner and let the user know if they guessed correctly or not
    if winners[0]:
        if predictedWinner == "tom":
            print "You guess right!"
        else:
            print "You guessed wrong"
        print "Tom won the race"
    elif winners[1]:
        if predictedWinner == "sally":
            print "You guess right!"
        else:
            print "You guessed wrong"
        print "Sally won the race"
    elif winners[2]:
        if predictedWinner == "fred":
            print "You guess right!"
        else:
            print "You guessed wrong"
        print "Fred won the race"

main()