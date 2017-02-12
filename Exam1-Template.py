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

def getAverage(speeds):
    ave = sum(speeds) / float(len(speeds))
    ave = float("{0:.2f}".format(ave)) #rounds the ave to 2 decimal points
    return ave

    
# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(speeds, maxSpeed):
    maxSpeed = 69
    s = 0
    for x in speeds:
        if (x > maxSpeed):
            s += 1
    return s


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
    speeds = readData('data-rush.txt')
    rave = getAverage(speeds)
    rs = countSpeeders(speeds, 69)
    rfine = rs * 150
   
    speeds = readData('data-not-rush.txt')
    nrave = getAverage(speeds)
    nr = countSpeeders(speeds, 69)
    nrfine = nr * 100

    print "The average speed during rush hour was %s " %rave
    print "The average speed not during rush hour was %s" %nrave
    print "There were %s speeders during rush hour. Total fine = $%s" % (rs, rfine)
    print "There were %s speeders not during rush hour. Total fine = $%s" % (nr, nrfine)
    
# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()