import func

song = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17] 

#adds the user input in each variable as a string
firstVerse = func.userString("Enter the first verse:") 
secondVerse = func.userString("Enter the second verse:")
thirdVerse = func.userString("Enter the third verse:")
fourthVerse = func.userString("Enter the fourth verse:")
chorus = func.userString("Enter the chorus:") + " " 
repeat = func.userInt("Enter the chorus repeat:")

#replaces the place holders in the list with user's input
song[0] = firstVerse
song[1] = chorus * repeat
song[2] = secondVerse
song[3] = chorus * repeat
song[4] = thirdVerse
song[5] = chorus * repeat
song[6] = fourthVerse
song[7] = chorus * repeat + chorus
song[8] = ("...One More Time!...")
song[9] = firstVerse
song[10] = chorus * repeat
song[11] = secondVerse
song[12] = chorus * repeat
song[13] = thirdVerse
song[14] = chorus * repeat
song[15] = fourthVerse
song[16] = chorus * repeat + chorus

print song

#prints out the new varibles in the list
print
for x in song:
    print(x)

