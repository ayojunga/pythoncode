import json
import func

def getJson():
    jsonTxt = ""
    f = open('contacts.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    contacts = json.loads(jsonTxt)
    
    return contacts

def userInput(contacts):
    name = func.userString("Enter a professor's name ('Mark Cohen', 'David Eve', 'Spencer Moser', 'Karen Cardozo', 'Yunus Umarov'):")
    for contact in contacts:
        if contact["Professor"] == name:
            for email in contact["Email"]:
                print "\nEmail: %s" %email
                print "Office Hours: %s" % contact["Hours"]
                print "Favorite Food: %s" % contact["Food"]
                print "Hobby: %s" % contact["Hobby"]
            

def main():
    print "List of professors with their contact information and office hours"
    userInput(getJson())

main()
    