# ------------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings.
#
# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type 
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------
def countBirds(filename):
    firstBird = True
    birds = {}
    for line in open("birds.txt"):
        birdFound = True
        temp = line.split(",")
        name = temp[0].strip()
        seen = int(temp[1].strip())
        #this adds the first bird no matter what, so that the for loop can run
        if firstBird:
            birds[name] = seen
            firstBird = False
        #if the bird found is found its value will be incremented
        for key in birds:
            if key == name:
                birds[name] += seen
                birdFound = True
                break
            birdFound = False
        #if it cant find the bird in the dictionary it will add it 
        if not birdFound:
            birds[name] = seen
            
    return birds
    
# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    print "Enter the name of the bird: "
    #takes the user input and capitalizes the first letter of the bird name
    n = raw_input().upper().title()
    
    #checks to see if the value is greater than one to determine whether to print "time" or "times"
    time = 'times' if d[n] > 1 else 'time'
    print "I have seen that bird {} {}".format(d[n], time)

def main():
    askUser(countBirds("birds.txt"))
    
    
main()