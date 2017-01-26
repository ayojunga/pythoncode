import func

song = []

#adds the user input in each variable as a string
firstVerse = func.userString("Enter the first verse:") 
secondVerse = func.userString("Enter the second verse:")
thirdVerse = func.userString("Enter the third verse:")
fourthVerse = func.userString("Enter the fourth verse:")
chorus = func.userString("Enter the chorus:") + " " 
repeat = func.userInt("Enter the chorus repeat:")

#adds the strings to the list
song.append(firstVerse)
song.append(chorus * repeat)
song.append(secondVerse)
song.append(chorus * repeat)
song.append(thirdVerse)
song.append(chorus * repeat)
song.append(fourthVerse)
song.append(chorus * repeat + chorus)
song=song*2

#inserts the string in the middle of the list
song.insert(8, "...One More Time!...")

#prints the list and the values in it
print song
for x in song:
    print (x)

