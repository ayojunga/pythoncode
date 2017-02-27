def countPpl(filename):
    cube = []
    square = []
    advanced = []
    inter = []
    avr = []
    path = []
    #separates the file and adds the values in the dictionary
    for line in open(filename):
        temp = line.split(",")
        name = temp[0].strip()
        time = float (temp[1].strip())
        
        #puts the name of the people in their corresponding arrays
        if time >= 0 and time < 10:
            cube.append(name)
        elif time >= 10 and time < 20:
            square.append(name)
        elif time >=20 and time < 30:
            advanced.append(name)
        elif time >=30 and time < 40:
            inter.append(name)
        elif time >= 40 and time < 60:
            avr.append(name)
        elif time >= 60:
            path.append(name)
    
    #put the list of arrays in a tuple
    return (cube, square, advanced, inter, avr, path)
   
  
def printList(string, array):
    #takes in a string and an array
    print string
    #prints each name in the array
    for name in array: print '      ' + name
    print ''


def main():
    lists = countPpl("timings.txt")
    
    #prints out the list of names in the arrays
    printList('Cube Head (0 - 9.99):', lists[0])
    printList('Square Master (10 - 19.99):', lists[1])
    printList('Advanced Twister (20 - 29.99):', lists[2])
    printList('Intermediate Turner (30 - 39.99):', lists[3])
    printList('Average Mover (40 - 59.99):', lists[4])
    printList('Pathetic (60 and above):', lists[5])
    
main()
  
    
