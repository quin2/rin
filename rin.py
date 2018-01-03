#todo: run clustering, make gui
import sys
import random
import pickle
from pathlib import Path

print("hello rin")

emotions = [
  "anger",
  "annoyance",
  "contempt",
  "disgust",
  "irritation",
  "anxiety",
  "embarrassment",
  "fear",
  "helplessness",
  "powerlessness",
  "worry",
  "doubt",
  "envy",
  "frustration",
  "guilt",
  "shame",
  "boredom",
  "despair",
  "disappointment",
  "hurt",
  "sadness",
  "shock",
  "stress",
  "tension",
  "amusement",
  "delight",
  "elation",
  "excitement",
  "happiness",
  "joy",
  "pleasure",
  "affection",
  "empathy",
  "friendliness",
  "love",
  "courage",
  "hope",
  "pride",
  "satisfaction",
  "trust",
  "calm",
  "content",
  "relaxed",
  "relieved",
  "serene",
  ]

targetLinkages = 5

fileName = "train.rin"
dataFileName = "data"

#get input character from console
def getInput():
    dec = input("answer [y/x/n]: ")

    if dec != 'y' and dec != 'x' and dec != 'n':
        getInput()

    return dec

#create blank array for filling on first run of rin
def createArray():
    toReturn = []
    for emotion in range(len(emotions)): toReturn +=[[0.0] * len(emotions)]
    return toReturn

#load array from file
def loadArray():
    return pickle.load(open(fileName, "rb"))

#save array to file
def saveArray(toSave):
    pickle.dump(toSave, open(fileName, "wb"))
    return

#load # of times run from file
def loadData():
    if not Path(dataFileName).is_file():
        saveData(0)
    return pickle.load(open(dataFileName, "rb"))

#save # of times run to file
def saveData(toSave):
    pickle.dump(toSave, open(dataFileName, "wb"))
    return


#get and load all the input right here
randValues = []
links = []
linkValues = []
yesValues = []

while len(yesValues) < targetLinkages:
    #find new random number each time
    rand = random.randrange(len(emotions))
    y = 0;
    while(y < len(randValues)):
        if(randValues[y] == rand):
            rand = random.randrange(len(emotions))
            y = 0;
        else:
            y += 1;

    randValues.append(rand)

    #map inputted values to array, eventually to be transcribed to master array
    print("")
    print("are you feeling " + emotions[rand] + "?")
    y = getInput()

    if(y == 'y'):
        yesValues.append(rand)

    elif(y == 'n'):
        links.append(rand)
        linkValues.append(1.0)

    elif(y =='x'):
        links.append(rand)
        linkValues.append(0.5)

#load data from past sessions
if not Path(fileName).is_file():
    saveArray(createArray())

emotionData = loadArray()
currentNum = loadData() + targetLinkages

#move current session data to master array
#for idx, item in enumerate(links):
#    for item2 in links[idx + 1:]:
#        emotionData[item][item2] += linkValues[idx]
#        emotionData[item2][item] += linkValues[idx]

#move session into master, version 2
for idx, noVal in enumerate(links):
    for yesVal in yesValues:
        emotionData[noVal][yesVal] += linkValues[idx]
        emotionData[yesVal][noVal] += linkValues[idx]

saveArray(emotionData)
saveData(currentNum)

#print everything for transparency
print()
print("saved data")
for n in emotionData:
    print(n)

print(currentNum)
