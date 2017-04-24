import json
import urllib2
import func


def weather(weatherInfo):
    #print out all the outputs 
    print "\nHere is the current weather for {}, {}" .format(weatherInfo['location']['name'], weatherInfo['location']['region'])
    print "{} and {} degrees (F).".format ( weatherInfo['current']['condition']['text'],weatherInfo['current']['temp_f'])
    print "It really feels like {} degrees (F) though.\n" .format (weatherInfo['current']['feelslike_f'])


def getJson(link):
    jsonTxt = urllib2.urlopen(link).read()
    return json.loads(jsonTxt)
    

def main():
    #as long as the user keeps entering y the code will continue to run
    run = True
    while(run):
        userInput = func.userString("Please enter a zip code or city name:")
        #adds the user input at the end of the link to print get the weather in json
        weatherInfo = getJson('https://api.apixu.com/v1/current.json?key=f159b8380cac43d2b1c191629172903&q=' + userInput)
        weather(weatherInfo)
       
        again = func.userString("Want to check another location? (y/n): ")
        #if user enters n the code will stop running
        if(again == "n"):
            run = False


main()