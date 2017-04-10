import func
import os
import string

def readFiles():
    
    fileList = []
    
    files = os.listdir(".")
    #adds all the files that end in .txt into an array of files
    for fname in files:
        
        if '.txt' in fname:
            
            fileList.append(fname)
    
    return fileList


def searchFile(fname, word):
	count = 0
	#reads the file and removes all punctuaion from each line and separates the word
	for line in open(fname, "r"):
		no_punc = line.translate(None, string.punctuation)
		words = line.split(" ")
		#uppercases each line and prints the file name and the line
		for w in words:
			if word in w.upper():
				count += 1
				print '{}: {}'.format(fname, line.upper().strip())

	return count
	
	
def main():
	
	fileList = readFiles()
	word = func.userString("Enter a search term:").upper()
	count = 0
	
	#for each file it counts the total amount of times it saw the word and runs the function fileList
	for file in fileList:
		count += searchFile(file, word)

	print "\nI found {} results" .format(count)

	

main()