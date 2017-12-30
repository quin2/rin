#todo: find out how to make dictionary, 2D list!! or just preload everything smhhhh
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
  "shame ",
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
  "interest",
  "politeness",
  "surprise",
  ]

targetLinkages = 3

fileName = "train.rin"
dataFileName = "data"

#get input character from console
def getInput():
    dec = input("answer [y/x/n]: ")

    if dec != 'y' and dec != 'x' and dec != 'n':
        getInput()

    return dec

def createArray():
    toReturn = []
    for emotion in range(len(emotions)): toReturn +=[[0.0] * len(emotions)]
    return toReturn

def loadArray():
    return pickle.load(open(fileName, "rb"))

def saveArray(toSave):
    pickle.dump(toSave, open(fileName, "wb"))
    return

def loadData():
    if not Path(dataFileName).is_file():
        saveData(0)
    return pickle.load(open(dataFileName, "rb"))

def saveData(toSave):
    pickle.dump(toSave, open(dataFileName, "wb"))
    return


#get and load all the input right here
randValues = []
links = []
linkValues = []

while len(links) < targetLinkages:
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
        links.append(rand)
        linkValues.append(1.0)

    elif(y =='x'):
        links.append(rand)
        linkValues.append(0.5)

if not Path(fileName).is_file():
    saveArray(createArray())

emotionData = loadArray()
currentNum = loadData() + targetLinkages

#move information to master array
for idx, item in enumerate(links):
    for item2 in links[idx + 1:]:
        emotionData[item][item2] += linkValues[idx]
        emotionData[item2][item] += linkValues[idx]

saveArray(emotionData)
saveData(currentNum)

for n in emotionData:
    print(n)

print(currentNum)
