import json
import func

#checks to see whether to look for category or keyword
def searchJson(x, y):
    Store = openJson()
    x = x.title() 
    #looks by the category or keyword depending on what the user enters
    for product in Store:
        if y.title() == "Category":
            if product["Category"] == x:
                print "{} - ${}" .format (product["Product"], product["Price"])
        if y.title() == "Keyword":
            if x in product["Product"]:
                 print "%{} - ${}" .format (product["Product"], product["Price"])
    
#opens the json file
def openJson():
    jsonTxt = ""
    f = open('PetStore.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    store = json.loads(jsonTxt)
    return store

#takes user input and searches the json file by either category or keyword and prints out the result
def main():
    
    userInput = func.userString("Search by Category (C) or Keyword (K)?")
   
    if userInput.upper() =='C':
        y = "Category"
        x = func.userString("Enter a Category:")
    
    if userInput.upper() == 'K':
        y = "Keyword"
        x = func.userString("Enter a Keyword:")

    searchJson(x, y)
    
    
main()