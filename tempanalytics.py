def readTemps():
    #opens the file
    file = open('temps.txt') 
    temps = []
    for line in file:
        line = line.strip() #returns each line as a string
        line = float(line) #converts each line into a float
        temps.append(line) #puts each line into a list called temps
    return temps
    
def calculateAve(temps, start, stop):
    total = 0
    x = stop - start #to get the difference between the two indexes 
    for i in range(start,stop): #takes the average of the range of numbers specified
        total = total + temps[i] #adds the numbers together
    ave = total/x #divides the total by the range of numbers specified to give you the average
    return ave
    
def count(temps, start, stop):
    count = 0
    temps = temps [:stop] #counts the elements in the index of the range specified
    #each time it finds a positive number it will add 1 to the variable count
    for x in temps:
        if x > 0:
            count += 1
    return count
        
def main(): 
    temps = readTemps()
    ave81 = calculateAve(temps, 0, 81)
    ave35 = calculateAve(temps, 81, 116)
    count81 = count(temps, 0, 81)
    count35 = count(temps, 0, 94)
    print "During the first 81 years, the average deviation from the temperature anomaly is %s" %ave81
    print "During the first 81 years, %s " %count81 + "had a positive temperature anomaly"
    print "During the first 35 years, the average deviation from the temperature anomaly is %s" %ave35
    print "During the first 35 years, %s " %count35 + "had a positive temperature anomaly"
  
main()
    