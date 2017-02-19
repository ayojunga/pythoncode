# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    file = open(filename)
    speeds = []
    for line in file:
        line = line.strip()
        line = int(line) 
        speeds.append(line) 
    return speeds
    
# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
readData("data-rush.txt")

def getAverage(speeds):
    ave = 0.0
    ave = sum(speeds) / len(speeds)
    print ave

    
# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
#def countSpeeders(speeds, maxSpeed):


# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
    
    
# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
#main()