import func

def congratulate(suspects, weapons):
    print "\nCongratulations you have found the suspect and the weapon!"
    print "It was {} who used the {}" .format (suspects[0], weapons[0])
    print "Your work is greatly appreciated detective Cohen"
    

def main():
    #create lists needed
    suspects = ['Mr Green','Miss Scarlet','Col Mustard']
    weapons = ['Pipe','Candlestick','Wrench']
    results = possibleOutcomes(suspects, weapons)
    
    print "{} possible outcomes left" .format(len(results))
    
    #as long as the length of the list array is greater than 1 it will continue to run the loop
    while(len(results) > 1):
        
        userInput = func.userString("Is the clue about a weapon or a suspect (w or s)?").lower()
        
        #ask user input and remove it from the list
        if userInput == "w":
            
            userGuess = func.userString("Enter the weapon that was not used (%s):" % weapons).title()
            weapons.remove(userGuess)
        
        elif userInput == "s":
            
            userGuess = func.userString("Enter the innocent suspect (%s):" % suspects).title()
            suspects.remove(userGuess)
        
        else:
            
            print "\nInvalid input"
        
        #print the list and the outcomes
        results = possibleOutcomes(suspects, weapons)
        print "{} possible outcomes left" .format(len(results))
    
    congratulate(suspects, weapons)


def possibleOutcomes(suspects, weapons):
    
    results = []
    #creates a combination of a list of weapons and suspects
    for w in weapons:
        for s in suspects:
            results.append("{} {}" .format (w, s))
    
    return results
    

main()